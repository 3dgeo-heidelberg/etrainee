---
title: "E-TRAINEE Theme 5 - Spatio-temporal data fusion"
description: "This is the fifth theme within module 1."
dateCreated: 2022-08-01
authors: Andreas Mayr
contributors: Martin Rutzinger, TBD
estimatedTime: 1.5 hrs
---

# Theme 5 - Spatio-temporal data fusion

*Work in progress*

*Coming soon: Figures, references, quiz questions, ...*

## Introduction

In the first themes (mainly themes 1 and 2) you have learned about the characteristics of remote sensing time series (RSTS) from different sources. In each excercise or practical tutorial we have used data from a single source (mostly Sentinel-2). For capturing environmental dynamics, you may, however, also have identified some limitations related to the data characteristics, such as the native spatial, spectral or temporal resolution or data gaps due to cloud cover. This theme deals with possibilities of addressing such limitations by spatio-temporal data fusion.

**Objectives**

The objectives of this theme are to

* Understand why spatio-temporal data fusion is needed for analysing human-environment interactions
* Learn about important prerequisites of data fusion and the challenges typically encountered
* Overview some popular combinations and typical or innovative approaches to fuse data
* Get to know some use cases where the benefits of multi-modal data are leveraged by data fusion
* Practice one possible way to combine multi-modal data for observing human-environment interactions in a tutorial

**Supporting tutorial**

The theme is accompanied by a tutorial where you learn how to jointly analyse Sentinel-1 and Sentinel-2 data for monitoring the extent of a water surface at the example of the Grand Ethiopian Rennaissance Dam (GERD).

## Motivation and approaches for spatio-temporal fusion of remote sensing time series

### Needs and challenges

In remote sensing applications there are very often high expectations on monitoring phenomena with challenging characteristics, such as

* Small magnitudes of change (compared to the noise in our data or its resolution)
* Small object size (Can you detect colonization by individual trees in 30-m pixels?)
* Rapid changes or fluctuations compared to the frequency of observations
* Slow, gradual changes or trends over multiple decades (which are usually not covered by RSTS from a single system)
* Similarity of different phenomena in a remotely sensed feature space (e.g., similar spectral change due to a construction site and due to a landslide)

In many cases analysis of RSTS from a single source just does not contain enough information, either in terms of detail (resolution in any domain) or in terms of extent (spatially or temporally, i.e., the area covered is too small or the time series is too short). Given such issues we often get disappointed when we see how even sophisticated RSTS methods really perform, as the results may contain too much spatial, temporal or semantic uncertainty to make any reliable interpretation and to ground our decisions on it. Sometimes only a combination of data from different systems provides the desired results.

Therefore, we can try to perform a spatio-temporal fusion of data from different systems (sensors and platforms) that are resolving different phenomena or aspects of them (spatially, spectrally, and temporally). As a broad definition for data fusion we may use the one proposed by [Steinberg et al. (1999)](https://doi.org/10.1117/12.341367): "Data fusion is the process of combining data to refine state estimates and predictions." In the following, we will look at how this process can look like and which data is typically combined.

### Approaches and methods for data assimilation and fusion of remote sensing time series

The topic is quite large, but we try to give a concise overview of popular combinations and typical or innovative approaches to fuse spatio-temporal data data. 

First of all, multi-model data can be fused at different levels (see e.g. [Hu et al. 2021](https://doi.org/10.1016/j.ophoto.2021.100002)):

* Data assimilation and fusion of remote sensing time series (from different yet similar systems, e.g. Landsat 7/8, Sentinel-2, MODIS, …) followed by further analysis
* Post-classification (post-analysis) data fusion (suitable for an integration of classification results from more diverse sensors/input data)


**Data from different multispectral satellite systems**

Such RSTS types are among the most frequently combined, e.g.:

* Imagery from different Landsats make up an unprecedentedly long and consistent time series, which is used in numerous studies (mostly Landsat 4-9, including earlier ones is a bit more difficult). For detecting forest-cover change [Fortin et al. (2020)](https://doi.org/10.1016/j.rse.2019.111266) presented an interesting example of fusing a large and diverse set of data collections (back to Landsat 1) via post-classification data fusion (BULC approach and CART classifiers), including also a modification of the minimum mapping unit.
* Data from Landsat and Sentinel-2 satellites are similar in many aspects but they still require adjustments and homogenization for optimum fusion results. For Landsat 8 OLI and Sentinel-2 MSI data, you can readily use the surface reflectance products of the [Harmonized Landsat and Sentinel-2 (HLS) archive](https://lpdaac.usgs.gov/news/release-of-harmonized-landsat-and-sentinel-2-hls-version-20/) at (Landsat-native) 30-m resolution (Claverie et al. 2018, Franch et al. 2019, Gan et al. 2021).
* Sentinel-2 and MODIS, or (similarly) Landsat and MODIS (e.g. [Gevaert and García-Haro 2015](https://doi.org/10.1016/j.rse.2014.09.012), [Gao et al. 2017](https://doi.org/10.1016/j.rse.2016.11.004), [Moreno-Martínez et al. 2020](https://doi.org/10.1016/j.rse.2020.111901)), or Sentinel-2 and Sentinel-3 ([Wang and Atkinson 2018](https://doi.org/10.1016/j.rse.2017.10.046)) - These pairs are particularly attractive as they combine relatively high spatial and temporal resolutions.
* Planet (CubeSat), Landsat and MODIS data - While the Planet CubeSat system offers unprecedented spatio-temporal observing capacity, the relatively low radiometric quality and cross-sensor inconsistencies challenge its use. [Houborg and McCabe 2018](https://doi.org/10.1016/j.rse.2018.02.067) presented a multi-scale machine-learning method to radiometrically rectify multi-date CubeSat data into L8 consistent VNIR data.

**Data from active and passive sensing techniques**

A key limitation of passively sensed imagery (e.g., from Sentinel-2) is that the objects of interest are frequently obstructed by clouds, resulting in many gaps in a time series. Actively sensed data (such as Sentinel-1 data acquired with synthetic aperture radar (SAR)) can reduce this problem and a fusion of optical and SAR data might provide you with a substantively improved temporal resolution. See this [E-TRAINEE tutorial](./T5_water_surface_data_fusion.ipynb), where you learn how to implement such an approach for monitoring the extent of a water surface.


**3D Point clouds from different systems**

3D point clouds aacquired with different platforms and sensors may be combined to provide a more complete representation of a three-dimensional scene.  This can be especially attractive if complex terrain, vegetation and unfavourable viewing angles degrade the geometric quality or leave gaps in a single source point cloud. In this context, [Zieher et al. 2018](https://doi.org/10.5194/isprs-archives-XLII-2-1243-2018) presented methods for fusing point clouds from terrestrial laser scanning (TLS) and photogrammetry, respectively, thereby combining the advantages of the different measurement principles for landslide monitoring.


## Tutorial: Sentinel-1/-2 surface water monitoring

If you are finished with the theoretical part of this theme, you are ready to try a data fusion approach to monitoring the extent of a water surface in [this tutorial](./T5_water_surface_data_fusion.ipynb).

**Case study**

 With the [Grand Ethiopian Renaissance Dam (GERD)](https://en.wikipedia.org/wiki/Grand_Ethiopian_Renaissance_Dam) being constructed on the Blue Nile river in Ethiopia, filling of a large water reservoir for hydroelectric power production started in the year 2020. We will try to observe the surface water extent in the GERD reservoir area during the first filling phase in 2020. As the filling makes quite rapid progress during the rainy season (when clouds tend to obstruct the view for optical satellite sensors), we want to combine data from Sentinel-1 and -2 to keep track of the lake extent dynamics.

**Approach**

On the one hand, we will get a time series of Normalized Difference Water Index (NDWI) computed from Sentinel-2 optical bands in the Google Earth Engine (GEE). On the other hand, we will use a time series of Sentinel-1 C-band Synthetic Aperture Radar (SAR) data from the GEE, more specifically Ground Range Detected (GRD) backscatter intensity. Learn more about SAR characteristics and Sentinel-1 (in general and in the GEE) [here](https://doi.org/10.1109/MGRS.2013.2248301) and [here](https://developers.google.com/earth-engine/tutorials/community/sar-basics).

We will not directly fuse data from S-1 and S-2, instead we first apply a simple classification of water and non-water and then fuse the classified water time series. As water contrasts well with other surface types in both S-1 and S-2 features and the changes taking place are large, we can expect such a relatively simple approach to work reasonably well (but let's see). The goal is to get somethin like the figure below that informs us about the progress of reservoir filling with time.


<img src="media/water_surface_extent_s1_s2.png" title="Percentage of area covered by water based on data from Sentinel-1 and -2" width="300">


## References

*Coming soon*

...

Steinberg, A. N., Bowman, C. L., & White, F. E. (1999). Revisions to the JDL data fusion model. In Sensor fusion: Architectures, algorithms, and applications III (Vol. 3719, pp. 430-441). SPIE. https://doi.org/10.1117/12.341367, https://apps.dtic.mil/sti/pdfs/ADA391479.pdf
