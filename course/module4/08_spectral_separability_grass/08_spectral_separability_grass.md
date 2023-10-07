---
title: "E-TRAINEE: Seasonal spectral separability of selected grass species of the Krkonoše Mts. tundra ecosystem"
description: "This is the eighth theme within the Airborne Imaging Spectroscopy Time Series Analysis module."
dateCreated: 2023-09-30
authors:
contributors: 
estimatedTime: 
---

# Case study: Seasonal spectral separability of selected grass species of the Krkonoše Mts. tundra ecosystem

This case study focuses on the separability of different grass species in Krkonoše Mts. 
during the vegetation growing season. It is inspired by a study by Červená et al. (2020), 
where differences in optical properties of three grass species were investigated on three scale levels: 
green leaf spectra measured by the spectroradiometer ASD FieldSpec4 Wide-Res coupled with a contact probe in laboratory conditions (leaf level), 
canopy spectra measured by the same spectroradiometer using the fiber optic cable with a pistol grip in the field (canopy level), and hyperspectral image data acquired with the Nano-Hyperspec® fastened to the DJI Matrice 600 Pro drone (image level). 

## Objectives

The objectives of this case study are as follows:

* Test the separability of four grass species during the 2020 vegetation season at the image level using statistical tests for each wavelength; 

* separability analysis (Jeffries-Matusita distance) in R. 

To get familiar with the area of interest, see [Tundra vegetation monitoring in Krkonoše Mountains](../../data_usecases/usecase_grasses_krkonose.md) in the Use Cases and Data section of the course.

## Data

Hyperspectral images acquired with the Headwall Nano-Hyperspec® fastened to the DJI Matrice 600 Pro drone on June 16th, July 13th, and August 11th, 2020 (*Figure 1*) were resampled from 269 spectral bands to 54 bands (to eliminate noise and correlation in neighboring bands),
and ground sampling distance was reduced from 3 to 9 cm.
For every of the four dominant grass species (*Nardus stricta* (`nard`) and competitive grasses *Calamagrostis villosa* (`cv`), *Molinia caerulea* (`mol`), and *Deschampsia cespitosa* (`desch`)) 450 random pixels were selected (*Figure 1*).
Spectral curves for these pixels were extracted based on all three hyperspectral images. The results are in a table, where the first column is called `classname` and contains class values `desch`, `cv`, `mol`, and `nard`, and the rest are columns with reflectance for each band in each month (e.g., `b1_2006` is band 1 of image acquired in June 2020, etc.). 
Data [module4/case_study_spectral_separability_grass]() is available in three text files, each for every month (`Rin_grasses_2020_month.txt`).

<p align="center">
<img src="media/flood_plain_img1.PNG" title="Hyperspectral data acquired in June (upper left), July (upper right), and August (lower) 2020. In the August image, there are also 450 random pixels selected for each of the four studied species." alt="Figure 1" width="600"/>
</p>

*Figure 1. Hyperspectral data acquired in June (upper left), July (upper right), and August (lower) 2020. In the August image, there are also 450 random pixels selected for each of the four studied species.*

<p align="center">
<img src="media/flood_plain_img1.PNG" title="The first ten rows of the table containing exported reflectance for 450 randomly selected pixels for each species." alt="Figure 2" width="600"/>
</p>

*Figure 2. The first ten rows of the table containing exported reflectance for 450 randomly selected pixels for each species.*


## Methods

### Separability analysis – Jeffries-Matusita distance

Separability analysis is often performed on the training data to find out whether all the defined classes will be distinguishable from each other. It can also help to estimate the expected error in the classification for various feature (band) combinations. 
Separability measures include, for example, Euclidean distance, Transformed divergence, Mahalanobis distance and its improved variants, Bhattacharyya distance and Jeffries-Matusita distance; for formulas, see *Figure 3* [(Schowengerdt, 2007)](#references). 
We will use the Jeffries-Matusita distance (JM distance). 
This analysis expects a normal distribution of the input data. 
Be aware that there are two formulas (*Figure 3*) for computing this separability measure. 
The most used formula in remote sensing is the one without the square root (*Figure 3, variant 2*). 
This variant is also used in the ENVI software. It can take values in the range [0, 2], where values greater than 1.9 indicate good separability of the classes; in case of separability lower than 1, it is probably a good idea to combine classes. 
However, originally the formula was defined with the square root (*Figure 3, variant 1*), so it means the values in the range [0, √2]. 
This formula is used, for example, in package varSel in R (Dalponte et al., 2013). 
As it is open source [code](https://rdrr.io/cran/varSel/src/R/JMdist.R), you can easily edit the function to the variant 2 used in ENVI and [Richards (2013)](#references); see also *Code 1*.





<p align="center">
<img src="media/flood_plain_img1.PNG" title="Formulas for Mahalanobis, Bhattacharyya and Jeffries-Matusita distances." alt="Figure 3" width="600"/>
</p>

*Figure 3. Formulas for Mahalanobis, Bhattacharyya and Jeffries-Matusita distances. are means and C are covariance matrices. [(Richards, 2013; Schowengerdt, 2007)](#References).*




### ANOVA, Welch's t-test, Wilcoxon test


## Results

## Conclusions
In this case study, we proved that all four grass species are separable based on the given hyperspectral dataset in all compared months in a season (June, July, and August). 
However, separability based on JM distance is lower for *Nardus stricta* (`nard`) and *Molinia caerulea* (`mol`) in June and July and for *Deschampsia cespitosa* (`desch`) and *Nardus stricta* (`nard`) in August. 
The best separability in all months is reached for *Molinia caerulea* (`mol`) and *Calamagrostis villosa* (`cv`). 
Separability measured by JM distance based on only one band was generally lower. 
The species were usually inseparable at bands around 720 nm, where all the spectral curves meet. 
We showed that JM distance is a better indicator of class separability than the commonly used statistical tests such as Welch’s t-test or Wilcoxon rank test.

## References

Červená, L., Kupková, L., Potůčková, M., Lysák, J. (2020). SEASONAL SPECTRAL SEPARABILITY OF SELECTED GRASSES: CASE STUDY FROM THE KRKONOŠE MTS. TUNDRA ECOSYSTEM. Int. Arch. Photogramm. Remote Sens. Spat. Inf. Sci. XLIII-B3-2020, 371–376. [10.5194/isprs-archives-XLIII-B3-2020-371-2020](https://doi.org/10.5194/isprs-archives-XLIII-B3-2020-371-2020).

Dalponte, M., Orka, H.O., Gobakken, T., Gianelle, D., Naesset, E. (2013). Tree Species Classification in Boreal Forests With Hyperspectral Data. IEEE Trans. Geosci. Remote Sens. 51, 2632–2645. [10.1109/TGRS.2012.2216272](https://doi.org/10.1109/TGRS.2012.2216272).

Richards, J.A. (2013). Remote sensing digital image analysis: an introduction. Fifth edition. ed. Springer, Berlin.

Schowengerdt, R.A. (2007). Remote sensing, models, and methods for image processing. 3rd ed. ed. Academic Press, Burlington, MA.

### Back to the start  
Proceed with a case study on [discrimination of selected grass species from time series of RPAS hyperspectral imagery](../06_Krkonose_tundra_grasslands/06_Krkonose_tundra_grasslands.md)

