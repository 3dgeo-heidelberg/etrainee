"""Preprocess imagery in RAM for use in convolutional neural nets."""
import numpy as np
from osgeo import gdal
from scipy.io import loadmat


class Image_reader:
    """Read the imagery into RAM."""

    def __init__(self, train_dir, reference_dir, is_training=False,
                 nodata_img=[], nodata_gt=0):
        """Initialise the class with required data."""
        self.is_training = is_training
        self.train_dir = train_dir
        self.nodata_img = nodata_img
        if self.is_training:
            self.reference_dir = reference_dir
            self.nodata_gt = nodata_gt
        pass


class Image_tiler:
    """Tile imagery in RAM for use in convolutional neural nets."""

    def __init__(self, in_arr, out_shape=(256, 256),
                 out_overlap=128, offset=(0, 0)):
        """
        Initialize the class with required data.

        in_arr:         the numpy array to tile
        out_shape:      tuple of (height, width) of resulting tiles
        out_overlap:    int, number of pixels to overlap by
        offset:         tuple, offset from top left corner in pixels
        """
        self.in_arr = in_arr
        self.in_shape = in_arr.shape
        self.out_shape = out_shape
        self.out_overlap = out_overlap
        self.offset = offset

    def crop_image(self):
        """Crops the input image in order to be tileable."""
        height = self.out_shape[0] + self.offset[0]
        while True:
            height += (self.out_shape[0] - self.out_overlap)
            if self.in_shape[0] < height:
                height -= (self.out_shape[0] - self.out_overlap)
                break

        width = self.out_shape[1] + self.offset[1]
        while True:
            width += (self.out_shape[1] - self.out_overlap)
            if self.in_shape[1] < width:
                width -= (self.out_shape[1]-self.out_overlap)
                break

        self.crop_arr = self.in_arr[self.offset[0]:height,
                                    self.offset[1]:width, :]
        return self.crop_arr

    def tile_image(self):
        """Tiles the input image in order to use it in CNNs."""
        self.tiles_num_ver = int((self.in_shape[0] - self.out_shape[0])
                                 / (self.out_shape[0] - self.out_overlap)) + 1
        self.tiles_num_hor = int((self.in_shape[1] - self.out_shape[1])
                                 / (self.out_shape[1] - self.out_overlap)) + 1

        tiles_num = self.tiles_num_ver * self.tiles_num_hor
        self.tiles_arr = np.empty((tiles_num, self.out_shape[0],
                                  self.out_shape[1], self.in_shape[2]),
                                  self.in_arr.dtype)
        idx = 0

        for row in range(self.tiles_num_ver):
            for col in range(self.tiles_num_hor):
                row_start = row * (self.out_shape[0] - self.out_overlap)
                col_start = col * (self.out_shape[1] - self.out_overlap)
                self.tiles_arr[idx, :, :, :] = self.in_arr[
                    row_start:row_start+self.out_shape[0],
                    col_start:col_start+self.out_shape[1], :]
                idx += 1
        return self.tiles_arr


def run_tiling(in_arr, out_shape=(256, 256), out_overlap=128, offset=(0, 0)):
    """Tile the image."""
    dataset = Image_tiler(in_arr, out_shape, out_overlap, offset)
    dataset.crop_image()
    dataset.tile_image()
    tiles_arr = dataset.tiles_arr
    del dataset
    return tiles_arr


def return_dimensions(in_arr, out_shape=(256, 256), out_overlap=128,
                      offset=(0, 0)):
    """Return the tiled dimensions."""
    dataset = Image_tiler(in_arr, out_shape, out_overlap, offset)
    dataset.crop_image()
    dataset.tile_image()

    dims = {
        'tiles_num': (dataset.tiles_num_ver, dataset.tiles_num_hor),
        'cropped_shape': dataset.crop_arr.shape
    }
    del dataset
    return dims


def read_gdal(trainingdata_path, referencedata_path):
    """Read data using gdal and transform into numpy array."""
    raster_orig = gdal.Open(trainingdata_path)
    raster_orig_arr = np.moveaxis(raster_orig.ReadAsArray(), 0, -1)
    raster_orig = None

    raster_gt = gdal.Open(referencedata_path)
    raster_gt_arr = np.expand_dims(raster_gt.ReadAsArray(), axis=-1)
    raster_gt = None

    arr_dict = {'imagery': raster_orig_arr,
                'reference': raster_gt_arr}
    return arr_dict


def read_gdal_with_geoinfo(trainingdata_path, offset=(0, 0)):
    """Read data using gdal and transform into numpy array."""
    def retrieve_geoinfo(img, offset):
        old_geot = img.GetGeoTransform()
        new_geot = (old_geot[0] + old_geot[1] * offset[0],
                    old_geot[1],
                    old_geot[2],
                    old_geot[3] + old_geot[5] * offset[1],
                    old_geot[4],
                    old_geot[5])
        geoinfo = {
            'projection': img.GetProjection(),
            'geotransform': new_geot
            }
        return geoinfo

    raster_orig = gdal.Open(trainingdata_path)
    raster_orig_arr = np.moveaxis(raster_orig.ReadAsArray(), 0, -1)
    raster_orig_geoinfo = retrieve_geoinfo(raster_orig, offset)
    raster_orig = None

    arr_dict = {'imagery': raster_orig_arr, 'geoinfo': raster_orig_geoinfo}
    return arr_dict


def read_pavia_centre(train_path, ref_path=None, out_shape=(1096, 1096, 102)):

    raster_orig = loadmat(train_path)
    raster_orig_arr = raster_orig['pavia']
    imagery = np.zeros(out_shape, dtype=np.uint16)
    imagery[:, :223, :] = raster_orig_arr[:out_shape[0], :223, :out_shape[2]]
    imagery[:, 605-(1096-out_shape[1]):, :] = raster_orig_arr[:out_shape[0], 224:, :out_shape[2]]
    arr_dict = {'imagery': imagery}

    if ref_path is not None:
        raster_gt = loadmat(ref_path)
        raster_gt_arr = raster_gt['pavia_gt'][:, :, None]
        reference = np.zeros([out_shape[0], out_shape[1], 1], dtype=np.uint8)
        reference[:, :223, :] = raster_gt_arr[:out_shape[0], :223, :]
        reference[:, 605-(1096-out_shape[1]):, :] = raster_gt_arr[:out_shape[0], 224:, :]
        arr_dict['reference'] = reference

    arr_dict['geoinfo'] = {}
    return arr_dict


def run_tiling_dims(in_arr, out_shape=(256, 256), out_overlap=128,
                    offset=(0, 0)):
    """Tile the image."""
    dataset = Image_tiler(in_arr, out_shape, out_overlap, offset)
    dataset.crop_image()
    dataset.tile_image()

    tiles_arr = dataset.tiles_arr
    dims = {
        'tiles_num': (dataset.tiles_num_ver, dataset.tiles_num_hor),
        'cropped_shape': dataset.crop_arr.shape
    }

    del dataset
    out_dict = {'imagery': tiles_arr, 'dimensions': dims}
    return out_dict


def tile_training(in_dict, shape, overlap, offset=(0, 0)):
    """Tile the imagery for training."""
    tiled_imagery = run_tiling_dims(in_dict['imagery'], out_shape=shape,
                                    out_overlap=overlap, offset=offset)
    tiled_reference = run_tiling_dims(in_dict['reference'], out_shape=shape,
                                      out_overlap=overlap, offset=offset)
    out_dict = {
        'imagery': tiled_imagery['imagery'],
        'reference': tiled_reference['imagery']}
    return out_dict


def filter_useful_tiles(arr_dict, nodata_vals=[], min_usable_area=1.,
                        is_training=False, nodata_gt=0):
    """Filter only tiles with reference information."""
    idxs_keep = []

    if is_training:
        for idx, tile in enumerate(zip(arr_dict['imagery'],
                                       arr_dict['reference'])):
            ref_unique = np.unique(tile[1]).tolist()
            if nodata_gt in ref_unique:
                ref_unique.remove(nodata_gt)
                if len(ref_unique) > 0:
                    idxs_keep.append(idx)
            else:
                idxs_keep.append(idx)

        arr_dict = {
            'imagery': arr_dict['imagery'][idxs_keep],
            'reference': arr_dict['reference'][idxs_keep]
            }

    else:
        for idx, tile in enumerate(arr_dict['imagery']):
            ref_unique = np.unique(tile).tolist()
            if nodata_vals[0] in ref_unique:
                ref_unique.remove(nodata_vals[0])
                if len(ref_unique) > 0:
                    idxs_keep.append(idx)
            else:
                idxs_keep.append(idx)

        arr_dict = {'imagery': arr_dict['imagery'][idxs_keep]}

    return arr_dict


def normalize_tiles(in_dict, nodata_vals=[], is_training=False):
    """Normalize values between 0 and 1."""
    def normalize_input(arr):
        # normalize all values in array
        arr_norm = (arr - arr.min()) / (arr.max() - arr.min())
        return arr_norm
    arr_dict = {}
    arr_dict['imagery'] = in_dict['imagery'].transpose([0, 3, 1, 2])
    for nodata_val in nodata_vals:
        arr_dict['imagery'][arr_dict['imagery'] == nodata_val] = 0
    arr_dict['imagery'] = normalize_input(arr_dict['imagery']
                                          .astype(np.float32))
    if is_training:
        ref_newshape = in_dict['reference'].shape[:-1]
        arr_dict['reference'] = in_dict['reference'].reshape(ref_newshape)
        arr_dict['reference'] = arr_dict['reference'].astype(np.int64)
        unique, counts = np.unique(arr_dict['reference'], return_counts=True)
        return arr_dict, unique, counts
    else:
        return arr_dict


def normalize_tiles_1d(in_dict, nodata_vals=[], is_training=False):
    """Normalize values between 0 and 1."""
    arr_dict = {}
    if is_training:
        norm_dict, _, _ = normalize_tiles(in_dict, nodata_vals, is_training)
        arr_dict['imagery'] = norm_dict['imagery'][:, None, :, 0, 0]
        arr_dict['reference'] = norm_dict['reference'][:, 0, 0]
        arr_dict['reference'] = arr_dict['reference'] - 1
        unique, counts = np.unique(arr_dict['reference'], return_counts=True)
        return arr_dict, unique, counts
    else:
        norm_dict = normalize_tiles(in_dict, nodata_vals, is_training)
        arr_dict['imagery'] = norm_dict['imagery'][:, None, :, 0, 0]
        return arr_dict


def normalize_tiles_3d(in_dict, nodata_vals=[], is_training=False):
    """Normalize values between 0 and 1."""
    arr_dict = {}
    if is_training:
        norm_dict, _, _ = normalize_tiles(in_dict, nodata_vals, is_training)
        arr_dict['imagery'] = norm_dict['imagery'][:, None, :, :, :]
        arr_dict['reference'] = norm_dict['reference']
        unique, counts = np.unique(arr_dict['reference'], return_counts=True)
        return arr_dict, unique, counts
    else:
        norm_dict = normalize_tiles(in_dict, nodata_vals, is_training)
        arr_dict['imagery'] = norm_dict['imagery'][:, None, :, :, :]
        return arr_dict


"""
if __name__ == '__main__':
    dummy_filename = 'C:\\Users\\dd\\Pictures\\DSC_0084.jpg'
    dummy_arr = imageio.imread(dummy_filename)  # .astype(np.float32)

    print(dummy_arr.dtype)
    print(dummy_arr.shape)

    dummy_dataset = Image_tiler(dummy_arr, (256, 256), 128, (0, 0))
    dummy_crop = dummy_dataset.crop_image()
    print(dummy_crop.shape)
    dummy_tiles = dummy_dataset.tile_image()
    print(dummy_tiles.shape)
"""
