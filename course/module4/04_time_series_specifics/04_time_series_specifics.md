---
title: "E-TRAINEE: Specific features of airborne imaging spectroscopy analysis"
description: "This is the fourth theme within the Airborne Imaging Spectroscopy Analysis module."
dateCreated: 2021-03-28
authors:
contributors:
estimatedTime:
---

# Machine learning in imaging spectroscopy

**UNDER CONSTRUCTION. COMING SOON.**


## Objectives

In this theme, you will learn about:

* spectral endmembers
* spectral mixtures, pixel purity indices
* classification methods suitable for hyperspectral imagery (SAM, SVM, SFF, spectral unmixing, CNN, etc.)
* monotemporal vs. multitemporal classification – multitemporal composite (multiseasonal, interannual)
* different number/combinations of seasonal images
* training data and its use for multitemporal classification (number and spatial distribution of training data, combination of training data from different dates/years)
* methods of classification results validation
* definition of change, change vs. error

After finishing this theme you will be able to:

* Classify multitemporal data using different machine learning methods in R or Python.


## Methods



## Examples



## Exercise

### Subpixel classification

The aim of this exercise is to explore the possibilities of subpixel classification, namely the different methods of endmember collection, regression-based spectral unmixing, and evaluation of the resulting species maps.

Please proceed to the exercise: [Subpixel classification](04_time_series_specifics_exercise_subpixel.md).

### Machine Learning classification

The aim of this exercise is to classify a hyperspectral image using two machine learning classifiers, Support Vector Machine (SVM) and Random Forest (RF). Then you will comapre the classifiers and observe how changing hyperparameter values alters the result.

Please proceed to the exercise: [Machine Learning classification](04_time_series_specifics_exercise_ml.ipynb).

### Convolutional Neural Network (CNN) classification

The aim of this exercise is to get acquainted with 1D, 2D and 3D Convolutional Neural Networks, in order to understand how different network structures extract spectral, spatial and spectro-spatial information and how that influences the resulting classification.

Please proceed to the exercise: [CNN classification](04_time_series_specifics_exercise_cnn.md).


### Next unit
Proceed with [Temporal vs. spatial and spectral resolution](../05_specific_resolution_contribution/05_specific_resolution_contribution.md)


## References

### Key literature


### Further articles and referenced literature