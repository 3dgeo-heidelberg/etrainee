---
title: "E-TRAINEE: Exploration of hyperspectral data - report"
description: "This is an example of report for the first exercise within the Airborne Imaging Spectroscopy Time Series Analysis module."
dateCreated: 2022-05-26
authors:
contributors: 
estimatedTime: 
---


## Report

#### 1. First encounter with data

##### Load and visualize image
In the first part of the exercise, I've been working with an image of a mountain pine with the tag `LH_mountain_pine_1_2020_08`.

##### EnMAP-Box capabilities
<center>
<img src="media/report_google_maps.png" alt="Added WMS Layer" title="Added WMS Layer" width="600">
 
<i>Added WMS layer of Google Satellite Maps</i>
</center>

<center>
<img src="media/report_image_statistics.png" alt="Image Statistics" title="Image Statistics" width="600">
 
<i>Histogram and statistics of band 108</i>
</center>

##### Spectral curves
<center>
<img src="media/report_spectral_curve_light.png" alt="Spectral Curve - Light Pixel" title="Spectral Curve - Light Pixel" width="600">
 
<i>Spectral curve of a light pixel</i>
</center>

<center>
<img src="media/report_spectral_curve_shadow.png" alt="Spectral Curve - Dark Pixel" title="Spectral Curve - Dark Pixel" width="600">

<i>Spectral curve of a shadowed pixel </i>
</center>

<center>
<img src="media/report_spectral_curve_multiple.png" alt="Spectral Curves" title="Spectral Curves" width="600">

<i>Multiple spectral curves with 5x5 mean sampling</i>
</center>

#### 2. Comparison of spectral characteristics

##### Spectral curves for classes and subclasses

| Class | Subclass | Spectral curve |
| :-- | :-- | :--: |
| mountain pine | | <img src="media/report_spectral_curve_mountain_pine.png" alt="Spectral Curve - Mountain Pine" title="Spectral Curve - Mountain Pine" width="300"> |
| scree | | <img src="media/report_spectral_curve_scree.png" alt="Spectral Curve - Scree" title="Spectral Curve - Scree" width="300"> |
| grass | Deschampsia cespitosa | <img src="media/report_spectral_curve_grass_deschampsia_cespitosa.png" alt="Spectral Curve - Grass Deschampsia cespitosa" title="Spectral Curve - Grass Deschampsia cespitosa" width="300"> |
| grass | Nardus stricta | <img src="media/report_spectral_curve_grass_nardus_stricta.png" alt="Spectral Curve - Grass Nardus stricta" title="Spectral Curve - Grass Nardus stricta" width="300"> |
| shrub | Vaccinium myrtillus | <img src="media/report_spectral_curve_shrub_vaccinium_myrtillus.png" alt="Spectral Curve - Shrub Vaccinium myrtillus" title="Spectral Curve - Shrub Vaccinium myrtillus" width="300"> |
| shrub | Calluna vulgaris | <img src="media/report_spectral_curve_shrub_calluna_vulgaris.png" alt="Spectral Curve - Shrub Calluna vulgaris" title="Spectral Curve - Shrub Calluna vulgaris" width="300"> |

The most significant difference can be seen between the spectral curve of class scree and all the other classes representing vegetation. The spectral curve of class scree gently increases with wavelength, in contrast to spectral curves of vegetation. 
Vegetation classes reach lower values until the break around 700 nm, where the curves turn to even higher values than scree.
In general, for the identification of scree, one can use a threshold value of wavelength lower than 700 nm or a ratio of values of wavelength higher and lower than 700 nm.
A low ratio indicates scree, a high ratio is typical for vegetation.

<center>
<img src="media/report_comparison_mountain_pine_scree.png" alt="Spectral Curves - Comparison of Mountain Pine and Scree" title="Spectral Curves - Comparison of Mountain Pine and Scree" width="400">

<i>Comparison of spectral curves of mountain pine (jump in values) and scree (gentle increase)</i>
</center>

Description of the differences between vegetation classes is much more complicated because the spectral curves are very similar. 
Some of them reach lower values in the near infrared part of the spectrum, e.g. mountain pine and shrub Calluna vulgaris. 
Comparing the two subclasses of grass, there are less significant differences in the highest values.

<center>
<img src="media/report_comparison_grass_deschampsia_nardus.png" alt="Spectral Curves - Comparison of Grass Deschampsia cespitosa and Nardus stricta" title="Spectral Curves - Comparison of Grass Deschampsia cespitosa and Nardus stricta" width="400">

<i>Comparison of spectral curves of grass Deschampsia cespitosa (higher values) and Nardus stricta (lower values)</i>
</center>

##### Differences in spectral curves within classes
In this part of the exercise, I've been working with an image of Deschampsia cespitosa with the tag `LH_grass_deschampsia_cespitosa_1_2020_08`. 
As mentioned in the previous task, Deschampsia cespitosa seems to be distinguishable from Nardus stricta due to its higher reflectance values. Although the values are highly dependent on the chosen pixel.

<center>
<img src="media/report_multiple_spectral_curves_grass_deschampsia_nardus.png" alt="Spectral Curves - Grass Deschampsia cespitosa" title="Spectral Curves - Grass Deschampsia cespitosa" width="400">

<i>Spectral curves for various pixels of grass Deschampsia cespitosa</i>
</center>

##### Classification of additional images
| Name of image | Class |
| :-- | :-- |
| `unknown_1` | scree |
| `unknown_2` | mountain pine |
| `unknown_3` | shrub Calluna vulgaris |
| `unknown_4` | grass Nardus stricta |
| `unknown_5` | grass Deschampsia cespitosa |
| `unknown_6` | shrub Vaccinium myrtillus |

#### 3. Exploration of changes in spectral characteristics in time
| Class | Spectral curves | Comments |
| :-- | :--: | :-- |
| mountain pine | <img src="media/report_mountain_pine_months.png" alt="Spectral Curves - Mountain Pine in 4 Months" title="Spectral Curves - Mountain Pine in 4 Months" width="400"> | The highest values are from August, the lowest from June. In July and September, the reflectance is comparable. Shapes of the spectral curves are similar. |
| scree | <img src="media/report_scree_months.png" alt="Spectral Curves - Scree in 4 Months" title="Spectral Curves - Scree in 4 Months" width="400"> | Even though seasonal changes should not affect reflectance of scree, there are visible differences. The lowest values are from June. Shapes of the spectral curves are similar. |
| grass Deschampsia cespitosa | <img src="media/report_grass_deschampsia_cespitosa_months.png" alt="Spectral Curves - Grass Deschampsia Cespitosa in 4 Months" title="Spectral Curves - Grass Deschampsia Cespitosa in 4 Months" width="400"> | When compared to other vegetation classes, there is no rise in the spectral curve in June (lowest one) at 700 nm. The other curves are very similar, lower values are from September. |
| grass Nardus stricta | <img src="media/report_grass_nardus_stricta_months.png" alt="Spectral Curves - Grass Nardus Stricta in 4 Months" title="Spectral Curves - Grass Nardus Stricta in 4 Months" width="400"> | Again, the spectral curve from June (lowest one) is suspicious, but the others are almost identical, there are no differences between months. |
| shrub Calluna vulgaris | <img src="media/report_shrub_calluna_vulgaris_months.png" alt="Spectral Curves - Shrub Calluna Vulgaris in 4 Months" title="Spectral Curves - Shrub Calluna Vulgaris in 4 Months" width="400"> | In this case, the spectral curve from June is in the middle, but it differs from the others in that it rises slowly at 700 nm. The lowest one is from July. |
| shrub Vaccinium myrtillus | <img src="media/report_shrub_vaccinium_myrtillus_months.png" alt="Spectral Curves - Shrub Vaccinium Myrtillus in 4 Months" title="Spectral Curves - Shrub Vaccinium Myrtillus in 4 Months" width="400"> | The highest reflectance of the shrub in the near-infrared wavelengths is in July and the lowest in June. It seems as though the shrub has a shorter growing season than Calluna vulgaris. |

In general, images from June seem to have odd values of reflectance, which is evident from the spectral curves as well as visualization. For distinguishing between the classes, images from July or August are the most suitable.

### Back to theme
Proceed by returning to [Principles of imaging and laboratory spectroscopy](../01_spectroscopy_principles.md)