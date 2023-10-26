"""Tools for inference and geolocation of CNN RS results."""
import numpy as np
import torch
from osgeo import gdal


def combine_tiles_1d(model, data, t_shp, overlap, out_dims):
    """Combine resulting tiles."""
    def classify_tile(model_trained, tile):
        """Classify individual tiles."""
        pred = model_trained(tile.cuda()).cpu().detach().numpy()
        pred = pred[0, :].argmax(0).squeeze().astype(np.uint8)
        return pred

    crp_dims = out_dims['cropped_shape']
    tiles_num = out_dims['tiles_num']
    num_pixels = tiles_num[0] * tiles_num[1]
    print_interval = int(num_pixels/100)

    out_arr = np.empty((crp_dims[0], crp_dims[1]), np.uint8)
    print(f'Combining tiles to shape {crp_dims}')
    print('Model application at:')

    loader = torch.utils.data.DataLoader(data, batch_size=1)
    for idx, tile in enumerate(loader):
        if idx % print_interval == 0:
            print(f'{idx/num_pixels*100:.0f} %')

        tile_class = classify_tile(model, tile)

        xmin = idx // tiles_num[1]
        ymin = idx % tiles_num[1]
        out_arr[xmin:xmin+1, ymin:ymin+1] = tile_class

    out_arr = np.add(out_arr, 1)
    print('Largest index is:', tiles_num[0] * tiles_num[1] - 1)
    return out_arr


def combine_tiles_2d(model, data, t_shp, overlap, out_dims):
    """Combine resulting tiles."""
    def classify_tile(model_trained, tile):
        """Classify individual tiles."""
        pred = model_trained(tile.cuda()).cpu().detach().numpy()
        pred = pred[0, :, :, :].argmax(0).squeeze().astype(np.uint8)
        return pred

    crp_dims = out_dims['cropped_shape']
    tiles_num = out_dims['tiles_num']
    over = int(overlap/2)
    t_over = (int(t_shp[0] - over), int(t_shp[1] - over))
    t_small = (int(t_shp[0] - overlap), int(t_shp[1] - overlap))

    out_arr = np.empty((crp_dims[0], crp_dims[1]), np.uint8)
    print(f'Combining tiles to shape {crp_dims}')

    loader = torch.utils.data.DataLoader(data, batch_size=1)
    x, y, z, k = 1, 1, 1, 1
    for idx, tile in enumerate(loader):
        tile_class = classify_tile(model, tile)

        # top left corner
        if idx == 0:
            out_arr[:t_over[0], :t_over[1]] = \
                tile_class[:t_over[0], :t_over[1]]

        # top right corner
        elif idx == tiles_num[1] - 1:
            ymin = int(crp_dims[1] - t_over[1])
            out_arr[:t_over[0], ymin:crp_dims[1]] = \
                tile_class[:t_over[0], over:]

        # bottom left corner
        elif idx == (tiles_num[0] - 1) * tiles_num[1]:
            xmin = int(crp_dims[0] - t_over[0])
            out_arr[xmin:crp_dims[0], :t_over[1]] = \
                tile_class[over:, :t_over[1]]

        # bottom right corner
        elif idx == tiles_num[0] * tiles_num[1]-1:
            xmin = int(crp_dims[0] - t_over[0])
            ymin = int(crp_dims[1] - t_over[1])
            out_arr[-t_over[0]:, -t_over[1]:] = tile_class[over:, over:]

        # top row
        elif idx >= 0 and idx < tiles_num[1] - 1:
            ymin = int(t_small[0] * idx + over)
            ymax = ymin + t_small[0]
            out_arr[:t_over[1], ymin:ymax] = tile_class[:t_over[1],
                                                        over:t_over[0]]
            z += 1

        # bottom row
        elif idx > tiles_num[1] * (tiles_num[0] - 1) - 1 and \
                idx < tiles_num[1] * tiles_num[0]:
            ymin = int(t_small[1] * y + over)
            ymax = ymin + t_small[1]
            out_arr[-t_over[0]:, ymin:ymax] = tile_class[over:, over:t_over[1]]
            y += 1

        # left column
        elif idx % tiles_num[1] == 0:
            ymin = int(t_small[1] * x + over)
            ymax = ymin + t_small[1]
            out_arr[ymin:ymax, :t_over[0]] = \
                tile_class[over:t_over[1], :t_over[0]]
            x += 1

        # right column
        elif idx % tiles_num[1] == tiles_num[1]-1:
            ymin = int(t_small[1] * k + over)
            ymax = ymin + t_small[1]
            out_arr[ymin:ymax, -t_over[0]:] = tile_class[over:t_over[1], over:]
            k += 1

        else:
            xmin = idx // tiles_num[1] * t_small[0] + over
            ymin = idx % tiles_num[1] * t_small[1] + over
            out_arr[xmin:xmin+t_small[0], ymin:ymin+t_small[1]] = \
                tile_class[over:-over, over:-over]

    print('Largest index is:', tiles_num[0] * tiles_num[1] - 1)
    return out_arr


def export_result(out_path, arr, geoinfo):
    """Export combined results into file."""
    print(f'Creating GDAL raster of size {arr.shape} pixels.')
    driver = gdal.GetDriverByName('Gtiff')
    out_ds = driver.Create(out_path, xsize=arr.shape[1], ysize=arr.shape[0],
                           bands=1, eType=gdal.GDT_Byte,
                           options=['COMPRESS=LZW'])
    if geoinfo:
        out_ds.SetGeoTransform(geoinfo['geotransform'])
        out_ds.SetProjection(geoinfo['projection'])
    out_ds.GetRasterBand(1).WriteArray(arr)
    out_ds = None
    print('Exported succesfully')
