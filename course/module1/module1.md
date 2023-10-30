---
title: "E-TRAINEE Module 1"
description: "Module 1: Methods of Time Series Analysis in Remote Sensing"
dateCreated: 2023-04-14
authors: Andreas Mayr, Martin Rutzinger
contributors: E-TRAINEE development team
---

# Methods of Time Series Analysis in Remote Sensing

Module 1 covers a range of basic principles and methods of remote sensing time series analysis that are applicable to data from different platforms and sensors. While the hands-on parts of the module focus on optical satellite imagery, many of the approaches you learn here will be helpful for working with other data types (such as close-range imagery time series or time series of 3D point clouds from photogrammetry or laser scanning). Hence, in this module you will learn about:

* Principles of time series in general and remote sensing time series in specific
* Major Earth observation missions, data archives and access options
* Strategies and computing facilities for large remote sensing time series, including introductions with Python and with the Google Earth Engine
* Classification approaches and methods for remote sensing time series
* Trajectory-based views on remotely sensed variables
* Approaches to land surface monitoring and change detection
* Fusion of multi-modal remote sensing time series
* Possibilities and best practices for validating your analyses with remote sensing time series

## Structure overview

This module covers the following *themes*:

* [Principles of remote sensing time series](01_principles_of_remote_sensing_time_series/01_principles_of_remote_sensing_time_series.md)
* [Large time series datasets in remote sensing](02_large_time_series_datasets_in_remote_sensing/02_large_time_series_datasets_in_remote_sensing.md)
* [Time series analysis based on classification](03_time_series_analysis_based_on_classification/03_time_series_analysis_based_on_classification.md)
* [Trajectory-based analysis](04_trajectory-based_analysis/04_trajectory_based_analysis.md)
* [Spatio-temporal data fusion](05_spatio_temporal_data_fusion/05_spatio-temporal_data_fusion.md)
* [Reference data, validation and accuracy assessment](06_reference_data_validation_accuracy_assessment/06_reference_data_validation_accuracy_assessment.md)


## Prerequisites to perform this module

The following skills and background knowledge are required for this module:

* Basics of statistics
* Basics of geoinformation systems and handling raster/vector data
* Some familiarity with QGIS
* Basic programming skills in Python
* Principles of remote sensing


## Software

For the practical parts of this module (excercises and tutorials), you will need the software listed below. Follow the links to the individual software or tools, for help in setting them up.

* [QGIS](../software/software_qgis.md)
* [Python](../software/software_python.md)
    * To install the packages needed for the tutorials and excercises we recommend the package and environment management system [Conda](https://docs.conda.io/en/latest/)
    *  You can use the `etrainee_m1.yml` file to install the packages listed therein into a fresh Python environment. The yaml file can be downloaded here: <a href=../assets/python_envs/etrainee_m1.yml download>etrainee_m1.yml</a>.
* To reproduce the examples that are using [Google Earth Engine](https://earthengine.google.com/), a registered user account for this service is required (create one [here](https://earthengine.google.com/signup/), if you don't have one).


## Practical parts of this module (overview)

Module 1 contains at least one practical part (tutorial or excercise) per theme. The tutorials are linked as separate documents in the respective sections of a theme. Many of them are provided as Python Jupyter Notebooks and, if you download them, you can explore them interactively.

### Mandatory parts

It is recommended to go through the following tutorials and excercises (one per theme). They are focusing on image time series analysis with Python's `xarray` package and the Google Earth Engine (GEE) Python API, and they (partly) build upon each other:

* Theme 1
    * Tutorial 1: [Raster Time Series in Python using xarray](./01_principles_of_remote_sensing_time_series/T1_S2_xarray.ipynb), introducing the xarray package for handling labelled, multi-dimensional arrays at the example of a Sentinel-2 satellite image time series.
* Theme 2
    * Tutorial 1: [Sentinel-2 via STAC in Python](./02_large_time_series_datasets_in_remote_sensing/T2_Sentinel_STAC_v03.ipynb), showing how to access Sentinel-2 data via a SpatioTemporal Asset Catalog (STAC) and get it into the Python xarray processing framework.
* Theme 3
    * Tutorial 1: [Image time series classification in Python](./03_time_series_analysis_based_on_classification/T3_S2_landcover_classification.ipynb), showing a machine learning workflow with spectral-temporal metrics (derived from one season of satellite imagery) as features for landcover classification. The result is one landcover map (which we will validate in theme 6).
* Theme 4
    * Tutorial: [Forest disturbance assessment with Python and the GEE](./04_trajectory-based_analysis/T4_GEE_NDVI_time_series_points.ipynb), examining a Landsat 8 NDVI time series (spectral-temporal trajectory) to assess the timing of forest disturbance.
* Theme 5
    * Tutorial: [Sentinel-1/-2 surface water monitoring](./05_spatio_temporal_data_fusion/T5_water_surface_data_fusion.ipynb), where you learn how to combine Sentinel-1 SAR data and Sentinel-2 optical imagery for monitoring the extent of a water reservoir in a relatively simple workflow.
* Theme 6
    * Exercise: [Assessment of landcover classification accuracy](./06_reference_data_validation_accuracy_assessment/06_reference_data_validation_accuracy_assessment.md#exercise-assessment-of-landcover-classification-accuracy), with a solution provided in [this Notebook](./06_reference_data_validation_accuracy_assessment/T6_S2_landcover_classification_accuracy_solution.ipynb).

### Optional parts

In case you want to explore further topics and methods, there are more tutorials and excercises available:

* Theme 1
    * Tutorial 2: [Exploring a Sentinel-2 time series using QGIS and the GEE Timeseries Explorer plugin](./01_principles_of_remote_sensing_time_series/T1_QGIS_GEE_TS_Explorer.md)
    * Tutorial 3: [Explore temporal profiles of a vegetation index in Python with pandas](./01_principles_of_remote_sensing_time_series/T1_spectral-temporal_profiles.md)
    * Tutorial 4: [Exploring and processing a Sentinel-2 time series using the GRASS GIS temporal framework](./01_principles_of_remote_sensing_time_series/T1_GRASS_raster_time_series.md)
* Theme 2
    * Tutorial 2: [Google Earth Engine (GEE) in Python](./02_large_time_series_datasets_in_remote_sensing/T2_GEE_s2cloudless_v03_export_time_series.ipynb), showing how to use the GEE cloud computing environment and its Python API for accessing, cloud-masking and downloading a Sentinel-2 time series.
    * Tutorial 3: [Large point clouds in Python](./02_large_time_series_datasets_in_remote_sensing/PC_explore_v02.ipynb), providing a couple of hints for handling and exploring large point clouds efficiently in Python (so far not time-series specific).
    * Excercise: [Search and load Landsat data to QGIS via a STAC API](./02_large_time_series_datasets_in_remote_sensing/02_large_time_series_datasets_in_remote_sensing.md#excercise)
* Theme 3
    * Tutorial 2 with excercise:
        * The [Snow cover time series in Python tutorial](./03_time_series_analysis_based_on_classification/T3_S2_snow_classification.ipynb), introduces a very basic procedure for (binary) snow cover mapping with a Sentinel-2 time series. The result is a time series of snow cover maps.
        * Excercise: Based on the tutorial, try to interpret the spatial patterns of snow cover duration and investigate the sensitivity of the rule-based classification regarding the classification threshold. For a suggested solution to this excercise see the Notebook [Snow cover time series: Interpretation and sensitivity analysis](./03_time_series_analysis_based_on_classification/T3_S2_snow_classification__excercise.ipynb).


### Data credits

Landsat imagery courtesy of the [U.S. Geological Survey](https://www.usgs.gov/) / [Terms of use](https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits)

Copernicus Sentinel data courtesy of the [European Space Agency - ESA](https://www.esa.int/) / [Terms of use](https://scihub.copernicus.eu/twiki/do/view/SciHubWebPortal/TermsConditions)


### Start the module
... by proceeding to the first theme on [Principles of remote sensing time series](01_principles_of_remote_sensing_time_series/01_principles_of_remote_sensing_time_series.md).