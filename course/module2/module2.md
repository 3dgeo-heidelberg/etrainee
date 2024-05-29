---
title: "E-TRAINEE Module 2: Satellite Multispectral Images Time Series Analysis"
description: "Module 2 introduction"
authors: Adriana Marcinkowska-Ochtyra, Krzysztof Gryguc, Adrian Ochtyra
output: 
  github_document:
    pandoc_args: "--wrap=none"
---

E-TRAINEE Module 2: Satellite Multispectral Images Time Series Analysis
================

This Module aims to equip you with an in-depth understanding of **satellite multispectral imaging**, a potent tool that affords a unique perspective for observing and analyzing Earth’s surface. Through the capture of images across various wavelengths, satellite multispectral imaging allows for the identification and quantification of a broad spectrum of physical and biological phenomena.

Module 2 provides a diverse array of **pre-processing** and specific **analysis methods**, all thanks to the many opportunities afforded by multitemporal analysis of regularly captured, freely available satellite data. These methods pave the way for a plethora of applications in environmental studies. The selection of data and methods hinges on the study’s scale — whether local, regional, or global — and the required time interval to accurately capture phenomena of interest, such as the effects of hurricanes, climate change, or the peak of the growing season, in either inter-annual or intra-annual data. Thus, in this module, you will:

- grasp the fundamentals of multispectral imaging
- discover major sources and unique characteristics of Earth observation data
- understand how temporal aspect of satellite data can be used in different analyses on various scales
- learn the essential steps to prepare your images for analysis, including different corrections and maskings, as well as time series specific methods such as data harmonization, normalization, compositing, and gap filling
- dive into various approaches to the classification problems including machine learning algorithms and feature selection
- explore different approaches to detecting changes and disturbances in vegetation using change detection algorithms and methods
- apply the theoretical knowledge in the practical exercises to produce your own reference and image datasets and use them in classification and change detection problems
- conduct case study analyses with multispectral time series in different use cases

## Structure

This module is structured into the following themes:

- **[Principles of multispectral imaging](01_multispectral_principles/01_multispectral_principles.md)**  
- **[Temporal information in satellite data](02_temporal_information/02_temporal_information.md)**  
- **[Image processing](03_image_processing/03_image_processing.md)**  
- **[Multitemporal classification](04_multitemporal_classification/04_multitemporal_classification.md)**  
- **[Vegetation change and disturbance detection](05_vegetation_monitoring/05_vegetation_monitoring.md)**  
- **[Case study: Monitoring tundra grasslands (Karkonosze/Krkonoše Mountains)](06_cs_tundra_grasslands/06_cs_tundra_grasslands.md)**
- **[Case study: Effects of pollution in Ore Mountains](07_cs_forest_changes/07_cs_forest_changes.md)**
- **[Case study: Forest disturbance detection (Tatra Mountains)](08_cs_disturbance_detection/08_cs_disturbance_detection.md)**

## Prerequisites to perform this module

The following skills and background knowledge are required for this module.

- Basics of statistics
- Basics of geoinformation systems and handling raster/vector data
- Principles of remote sensing
- Basic programming skills (R and Google Earth Engine JavaScript will be used here)

Follow **[this link](../module0/module0.md)** for an overview of the listed prerequisites and recommendations on external material for preparation.

## Software

For this module, you will need the software listed below. If you did not install the software before starting the course, follow the links to the individual software or tools, for help in setting them up.

- **[QGIS](../software/software_qgis.md)** for visualization of time series satellite imagery and results of classification and change detection
- **[R language](../software/software_r_language.md)** for time series satellite imagery processing and analysis
- **[Google Earth Engine](../software/software_gee.md)** access (create an account **[here](https://earthengine.google.com/signup/)**)

## Use Cases and Data

### Use Cases

Research-oriented case studies in this module are introduced in **[Monitoring mountain vegetation in Karkonosze/Krkonoše Mountains (Poland/Czechia)](../data_usecases/usecase_tundra_karkonosze.md)**, **[Forest disturbances in Ore Mountains (Czechia)](../data_usecases/usecase_ore_mts_disturbance.md)** and **[Vegetation disturbance detection in Polish-Slovak Tatra Mountains](../data_usecases/usecase_forests_tatras.md)** use case documents. Familiarize yourself with them to have a better understanding of the analyses performed in Case Studies.

### Data

Data for the exercises is provided through [Zenodo](https://zenodo.org/records/10003575). Some input imagery is produced throughout the course. Below you can see the folder tree of data from Module 2.

    module2/
    ├───case_study_1
    │   │   README.txt
    │   ├───data_exercise/
    │   └───results/
    ├───case_study_3
    │   │   README.txt
    │   ├───data_exercise/
    │   └───results/
    ├───theme_1_exercise
    │   │   README.txt
    │   ├───data_exercise/
    │   └───results/
    ├───theme_2_exercise
    │   │   README.txt
    │   ├───data_exercise/
    │   └───results/
    ├───theme_4_exercise
    │   │   README.txt
    │   ├───data_exercise/
    │   └───results/
    └───theme_5_exercise
        │   README.txt
        ├───data_exercise/
        └───results/

Each folder in the main catalog contains short description of the data inside in `README.txt` file. Input data is provided in `data_exercise` folders. Empty (except Theme 1) `results` folders are provided to store the outputs. After downloading the packages you should follow the **[R language tutorial](../software/software_r_language.md)** to create an environment and start R project in the main `module2` catalog.

## Start the module

… by proceeding to the first theme on **[Principles of multispectral imaging](01_multispectral_principles/01_multispectral_principles.md)**
