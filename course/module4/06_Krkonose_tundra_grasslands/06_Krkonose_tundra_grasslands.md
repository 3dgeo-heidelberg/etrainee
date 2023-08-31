---
title: "E-TRAINEE: Case study Role of time series in the discrimination of selected grass species from RPAS hyperspectral imagery"
description: "This is the sixth theme within the Airborne Imaging Spectroscopy Time Series Analysis module."
dateCreated: 2021-03-28
authors:
contributors: 
estimatedTime: 
---

# Case study: monitoring tundra grasslands in the Krkonoše Mountains

## Introduction

This case study presents data, methods, and results elaborated in the Krkonoše Mts. National Park by our [TILSPEC](https://www.tilspec.cz) team at Charles University Prague, 
within the project “Development of methods for monitoring of the Krkonoše Mts. tundra vegetation changes using multispectral, hyperspectral and LIDAR sensors from UAV”. 
Important results of the project have been published in [Kupková et al. (2023)](#references). 
As we proved in this study, time series (in this case, a multitemporal UAV intra-seasonal dataset) can improve vegetation classification accuracy in comparison with one-date images. 
Following our research, the classification accuracy of selected tundra grass species derived from mono- and multitemporal (within one season) hyperspectral RPAS imagery is compared based on reference botanical datasets collected in the Krkonoše Mts. in 2020. 
Also tested is the influence of the pre-processing step, comprising the minimum noise fraction (MNF), on classification accuracy. The RF classification is carried out in R. 

<p align="center">
<img src="media/cskrnap_img1.PNG" title="Study area." alt="Figure 1" width="600"/>
</p>

*Figure 1. Image of study area near to Luční bouda hut in the Krkonoše Mts. National Park – permanent research plot Bílá louka meadow (red).*

## Objectives

* To classify grass vegetation in the Krkonoše Mts. on a permanent research plot 100 x 100 m (Figure 1) using Random Forest classifier (script in R) from UAV hyperspectral data acquired by the Headwall NANO-Hyperspec pushbroom camera.
  
* To evaluate and quantify a potential improvement in classification accuracy of the multi-temporal time series compared to mono-temporal imagery.
  
* To evaluate the influence of MNF transformation on the final classification result. (optional)

## Questions to be answered

* Is it possible to classify individual grass species from a mono-temporal UAS dataset with very high spatial resolution (9 cm) and spectral resolution (54 bands) with an overall accuracy higher than 85%?
  
* What is the classification accuracy of the dominant and sparse growth species?
  
* Can we reach higher accuracy using time series of intra-seasonal data? How significant are the differences?
  
* Optional: Can image data transformation that reduces noise and data dimensionality (MNF transformation) produce better results than the original hyperspectral dataset?

## Data

We will use:

* Hyperspectral image data acquired by the Headwall Nano-Hyperspec® camera fastened on the DJI Matrice 600 Pro drone on June 16 and August 11 2020 (Figure 2), with ground sampling distance of 9 cm and spectral resolution of 54 bands (resampled from 269 bands to reduce correlation in neighboring bands):  
            `BL_202006.tif (data from June; 54 bands, for visualization in true colors use bands R-21/G-13/B-7)`  
            `BL_202008.tif (data from August; 54 bands, for visualization in true colors use bands R-21/G-13/B-7)`  
            `BL_2020_0608MT.tif (multitemporal image – merged dataset from June and August; 108 bands)`

* Image data transformed using MNF transformation (10 bands, ground sampling distance 9 cm):  
            `BL_MNF_08_10 (10 output bands from MNF transformation)`

* Field reference dataset (*Figure 3*) collected by botanists (in 2019 and 2020) divided between training data (polygons) and validation data (points). For an explanation of how the reference dataset was collected and divided between training and validation data, see [Kupková et al. (2023)](#references):  
            `train_polygons.zip (training data)`  
            `valid_points.zip (validation data)`


<p align="center">
<img src="media/cskrnap_img2.PNG" title="Study area." alt="Figure 2" width="600"/>
</p>

*Figure 2. Hyperspectral data – imagery used for classification.*

<p align="center">
<img src="media/cskrnap_img3.PNG" title="Reference data." alt="Figure 3" width="600"/>
</p>

*Figure 3. Reference data – training polygons and an example of validation points.*


### Classification scheme

The classification scheme (*Figure 4*) includes four categories of dominant grass species: one originally common species (*Nardus stricta, NS*) and three currently expanding grasses *Calamagrostis villosa (CV), Molinia caerulea (MC)*, and *Deschampsia cespitosa*. Also, species with sparse growth on the permanent research plot were classified : *Avenella flexuosa (AFS), Carex bigelowii (CB)*, and *Picea abies (PAb)*.


<p align="center">
<img src="media/cskrnap_img4.PNG" title="Classified grassland species." alt="Figure 4" width="600"/>
</p>

*Figure 4. Classified grassland species.*

### Next unit
Proceed with a case study on [seasonal dynamics of flood-plain forests](../07_flood_plain_forest/07_flood_plain_forest.md)

