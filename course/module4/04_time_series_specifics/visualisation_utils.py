"""Set of functions for visualisations."""
import numpy as np
import torch
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from time import gmtime, strftime
from sklearn.metrics import confusion_matrix


def _create_colorlist_classnames(arr=None, ds_name='pavia_centre'):
	"""Return correct colormap and class names for plotting."""
	if ds_name == 'pavia_centre':
		color_list = ('white', 'blue', 'green', 'olive', 'red',
              'yellow', 'grey', 'cyan', 'orange', 'black')
		class_names = ('No Data', 'Water', 'Trees', 'Meadows', 'Self-Blocking Bricks',
			'Bare Soil', 'Asphalt', 'Bitumen', 'Tiles', 'Shadows')

	elif ds_name == 'lucni_hora':
		color_list = ('white', 'red', 'green', 'yellow', 'orange', 'purple',
            'blue', 'cyan', 'black', 'grey')
		class_names = ('No Data', 'Metlička Křivolaká',
            'metlička, tomka a ostřice',
            'brusnice borůvková', 'metlice trsnatá',
            'borovice kleč', 'smilka tuhá', 'kamenná moře bez vegetace',
            'vřes obecný', 'kameny, půda, mechy a vegetace')

	elif ds_name == 'bila_louka':
		color_list = ('white', 'red', 'green', 'yellow',
                      'orange', 'purple', 'blue', 'grey')
		class_names = ('No Data', 'afs', 'cv', 'cxbig',
                       'desch', 'mol', 'nard', 'smrk')

	else:
		print('Incorrect dataset name for creating a plot. Cannot create a colormap and a list of class names.')
		print('Valid dataset names are "lucni_hora", "bila_louka" or "pavia_centre".')

	if type(arr) is np.ndarray:
		arr_min, arr_max = np.min(arr), np.max(arr)
		out_cmap = color_list[arr_min:arr_max+1]
		out_class_names = class_names[arr_min:arr_max+1]
		return out_cmap, out_class_names

	else:
		return color_list, class_names


def _image_show(raster, title='Natural color composite'):
    """Show a figure based on a hyperspectral raster."""
    plt.imshow(raster/3000)
    plt.title(title)
    plt.axis('off')


def _class_show(raster, title, ds_name='pavia_centre'):
    """Show a figure based on a classification."""
    colorlist, classnames = _create_colorlist_classnames(raster, ds_name=ds_name)
    for label, color in zip(classnames, colorlist):
        plt.plot(0, 0, 's', label=label, alpha=1,
                 color=color, markeredgecolor='black')

    plt.imshow(raster, cmap=ListedColormap(colorlist), interpolation='nearest')
    # plt.colorbar(ticks=(np.linspace(0.5, 8.5, 10)))
    plt.title(title)
    plt.axis('off')
    # plt.legend()


def show_img_ref(hs_img, gt_img, ds_name='pavia_centre'):
    """Show the hyperspectral image and a training reference."""
    plt.figure(figsize=[16, 8])
    plt.subplot(1, 2, 1)
    _image_show(hs_img)
    plt.subplot(1, 2, 2)
    _class_show(gt_img, 'Reference data', ds_name=ds_name)
    plt.legend(ncol=3, bbox_to_anchor=(0.5, -0.15), loc='lower center')


def show_spectral_curve(tile_dict, tile_num, ds_name='pavia_centre',
                        title='Spectral curve for pixel #'):
    """Show a figure of the spectral curve."""
    # Choose a range of collected wavelengths
    if ds_name == 'krkonose':
        wl_min, wl_max = 404, 997
        plt.xlabel('Wavelength [nm]')
    else:
        wl_min, wl_max = 1, tile_dict["imagery"].shape[-1] + 1
        plt.xlabel('Band number')
    # Create a vector of wavelength values
    x = np.linspace(wl_min, wl_max, tile_dict["imagery"].shape[-1])

    # Read the spectral curve
    if len(tile_dict["imagery"].shape) == 4:
        y = tile_dict["imagery"][tile_num, 0, 0, :]
        lbl = tile_dict["reference"][tile_num, 0, 0, :][0] + 1
    elif len(tile_dict["imagery"].shape) == 3:
        y = tile_dict["imagery"][tile_num, 0, :]
        lbl = tile_dict["reference"][tile_num] + 1
    elif len(tile_dict["imagery"].shape) == 2:
        y = tile_dict["imagery"][tile_num, :]
        lbl = tile_dict["reference"][tile_num]
    else:
        print('The input data is in an incompatible shape.')

    _, classnames = _create_colorlist_classnames(ds_name=ds_name)

    plt.plot(x, y, label=f'{classnames[lbl]}')
    plt.title(f'{title} {tile_num}')
    plt.legend(bbox_to_anchor=(0.5, 0.89), loc='lower center')


def show_augment_spectral(tile_dict, tile_num, aug_funct, ds_name='pavia_centre'):
    """Show a figure of the original spectal curve and the augmented curve."""
    plt.figure(figsize=[8, 4])
    plt.subplot(1, 2, 1)
    show_spectral_curve(tile_dict, tile_num, ds_name=ds_name,
                        title='Original spectral curve for pixel #')
    plt.subplot(1, 2, 2)
    tensor_obs = torch.from_numpy(tile_dict["imagery"])
    tensor_gt = torch.from_numpy(tile_dict["reference"])
    aug_obs, aug_gt = aug_funct(tensor_obs, tensor_gt)
    aug_dict = {'imagery': aug_obs, 'reference': aug_gt}
    show_spectral_curve(aug_dict, tile_num, ds_name=ds_name,
                        title='Augmented spectral curve for pixel #')


def show_augment_spatial(tile_dict, tile_num, aug_funct, ds_name='pavia_centre'):
    """Show a figure of the original and the augmented RGB composite."""
    img_rgb = tile_dict['imagery'][tile_num, [25, 15, 5], :, :]
    img_rgb_transposed = img_rgb.transpose((1, 2, 0))
    tile_gt = tile_dict['reference'][tile_num, :, :]
    plt.figure(figsize=[20, 5])

    plt.subplot(1, 4, 1)
    _image_show(img_rgb_transposed*20000, title='Original RGB composite')

    plt.subplot(1, 4, 2)
    img_hs = tile_dict['imagery'][tile_num, :, :, :]
    img_augmented, gt_augmented = aug_funct(torch.from_numpy(img_hs),
                                 torch.from_numpy(tile_gt[None, :, :]))
    print(img_augmented.shape)
    img_augmented_np = np.array(img_augmented)
    img_aug_trans = img_augmented_np[0, [25, 15, 5], :, :].transpose(1, 2, 0)

    _image_show(np.array(img_aug_trans)*20000, title='Augmented RGB composite')

    plt.subplot(1, 4, 3)
    _class_show(tile_gt, 'Original reference data', ds_name=ds_name)
    plt.legend(ncol=3, bbox_to_anchor=(0.5, -0.15), loc='lower center')

    plt.subplot(1, 4, 4)
    _class_show(np.array(gt_augmented[0,:,:]), 'Augmented reference data', ds_name=ds_name)

def show_augment_spectro_spatial(tile_dict, tile_num, aug_funct, ds_name = 'pavia_centre'):
    """Show a figure of the original and the augmented RGB composite."""
    img_rgb = tile_dict['imagery'][tile_num, 0, [25, 15, 5], :, :]
    img_rgb_transposed = img_rgb.transpose((1, 2, 0))
    tile_gt = tile_dict['reference'][tile_num, :, :]
    plt.figure(figsize=[20, 5])

    plt.subplot(1, 4, 1)
    _image_show(img_rgb_transposed*20000, title='Original RGB composite')

    plt.subplot(1, 4, 2)
    img_hs = tile_dict['imagery'][tile_num, 0, :, :, :]
    img_augmented, gt_augmented = aug_funct(torch.from_numpy(img_hs),
                                 torch.from_numpy(tile_gt[None, :, :]))
    print(img_augmented.shape)
    img_augmented_np = np.array(img_augmented)
    img_aug_trans = img_augmented_np[0, 0, [25, 15, 5], :, :].transpose(1, 2, 0)

    _image_show(np.array(img_aug_trans)*20000, title='Augmented RGB composite')

    plt.subplot(1, 4, 3)
    _class_show(tile_gt, 'Original reference data', ds_name=ds_name)
    plt.legend(ncol=3)

    plt.subplot(1, 4, 4)
    _class_show(np.array(gt_augmented[0,:,:]), 'Augmented reference data',
		ds_name=ds_name)


def show_classified(hs_img, gt_img, class_img, ds_name='pavia_centre'):
    """Compare the classification result to the reference data."""
    plt.figure(figsize=[15, 5])
    plt.subplot(1, 3, 1)
    _image_show(hs_img)

    plt.subplot(1, 3, 2)
    _class_show(gt_img, 'Reference data', ds_name=ds_name)
    plt.legend(ncol=3)

    plt.subplot(1, 3, 3)
    _class_show(class_img, 'Classified data',
        ds_name=ds_name)


def show_confusion_matrix(gt, predict, ds_name='pavia_centre'):
    conf_matrix = confusion_matrix(gt, predict)

    fig, ax = plt.subplots(figsize=(7.5, 7.5))
    ax.matshow(conf_matrix, cmap=plt.cm.hot_r, alpha=0.3)
    # Add numbers to each position
    for i in range(conf_matrix.shape[0]):
        for j in range(conf_matrix.shape[1]):
            ax.text(x=j, y=i,s=conf_matrix[i, j], va='center', ha='center')

    # Make it look good
    ax.set_xlabel('Predicted labels')
    ax.xaxis.set_label_position('top')
    ax.set_ylabel('Reference labels')
    ax.set_title('Confusion matrix')

    _, classnames = _create_colorlist_classnames(ds_name=ds_name)
    classnames = classnames[-len(np.unique(predict)):]

    ax.set_xticks(np.arange(len(classnames)), labels=classnames)
    ax.set_yticks(np.arange(len(classnames)), labels=classnames)
    ax.tick_params(axis='x', labelrotation=90)

    plt.show()


def sec_to_hms(sec):
    """Convert seconds to hours, minutes, seconds."""
    ty_res = gmtime(sec)
    res = strftime("%Hh, %Mm, %Ss", ty_res)
    return str(res)
