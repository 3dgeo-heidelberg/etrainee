---
title: ""
description: ""
dateCreated: 2023-10-16
authors:
contributors:
estimatedTime:
---

# Exercise: Machine learning in imaging spectroscopy

Objective of this exercise is to compare results of different supervised classification methods applied on a hyperspectral (HS) image acquired with a Nano-Hyperspec® camera from an RPAS platform.

Methods based on reference spectra

* [Linear spectral unmixing](04_time_series_specifics_exercise_subpixel.md)
* [Spectral angle mapper (SAM)](04_time_series_specifics_exercise_sam.ipynb)
* [Spectral information divergence (SID – optional)](04_time_series_specifics_exercise_sid.ipynb)

A reference spectrum of each class in the image must be extracted/provided prior to classification. These methods are typically used in spectroscopy for data acquired with both spectroradiometers and imaging sensors.

Methods based on training samples

* [Random forest (RF)](04_time_series_specifics_exercise_rf.ipynb)
* [Support vector machine (SVM – optional)](04_time_series_specifics_exercise_svm.ipynb)
* Convolutional neural network (CNN – optional)
  - [3D CNN based on spectro-spatial convolution ](04_exercise_cnn_3d.ipynb)
  - [2D CNN based on spatial convolution (optional)](04_exercise_cnn_2d.ipynb)
  - [1D CNN based on spectral convolution (optional)](04_exercise_cnn_1d.ipynb)

SAM, SID, RF, SVM, and CNN classifications are provided as a Jupyter notebook or can be run through Google Colab, the EnMapBox is used for linear spectral unmixing. Each exercise can be done independently and comprises a set of tasks and a sample solution. Comparison of results of different classifications in QGIS is recommended.

See [next unit](#"Next unit")

### Dataset
The original dataset comprising 270 spectral bands and 3 cm ground sampling distance (GSD) acquired with a Nano-Hyperspec® camera mounted on DJI Matrice 600 Pro drone was resampled to 54 bands and 9cm GSD for the purpose of this exercise. It covers a 100 m x 100 m plot at the hillside of Luční hora in the Krkonoše mountains. The training and validation data were collected during the field campaign by botanists. The dataset was collected in August of 2020.

### Next unit
Proceed with [Temporal vs. spatial and spectral resolution](../05_specific_resolution_contribution/05_specific_resolution_contribution.md)