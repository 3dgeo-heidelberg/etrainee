---
title: "E-TRAINEE: Specific features of airborne imaging spectroscopy analysis"
description: "This is the fourth theme within the Airborne Imaging Spectroscopy Analysis module."
dateCreated: 2021-03-28
authors:
contributors:
estimatedTime:
---

# Machine learning in imaging spectroscopy

Image classification is one of basic processing steps in remote sensing aiming at the retrieval of thematic information (e.g., land cover types, vegetation species) from imagery. General introduction to image classification was given in Module 1 [Time series analysis based on classification](../module1/03_time_series_analysis_based_on_classification/03_time_series_analysis_based_on_classification.md) and Module 2 [Multitemporal classification](../module2/04_multitemporal_classification/04_multitemporal_classification.md). In this theme these concepts will be extended to a linear unmixing model basically allowing for a single-date classification with subpixel accuracy, spectral angle mapper (SAM), spectral feature fitting (SFF), and a convolutional neural network (CNN) model to classify mono- or multitemporal hyperspectral (HS) imagery.  

## Objectives

The objective of this theme is to learn about:
*	examples of classification methods suitable for HS imagery, namely linear spectral unmixing, SAM, and SID,
*	definition of spectral endmembers,
*	examples of CNN using different features for classification of HS imagery,
*	using the classification methods in multitemporal approach,
*	training and validation data distribution and accuracy assessment.

The theme ends with a self-evaluation quiz, a set of exercises, and a list of references.

In the practical exercise you will use linear spectral unmixing, CNN, and optionally also earlier learned random forest and support vector machine classifiers on an example of HS data collected at the Bílá louka and Luční hora plots of the Krkonoše Mountains National Park study site from an RPAS platform.

After finishing this theme, you will understand the principles of HS data classification and you will be able implement them in Python, R, or EnMapBox.

## Exercise

A set of classification algoritms is provided. While the algorithms based on reference spectra (linear unmixing, SAM, SID) are suitable for single date datasets and multitemporal analysis must be carried out on the classification results, the multitemporal datasets can be an input to present methods based on training samples (RF, SVM, CNN).

Proceed to the exercise: [Machine learning classification](04_time_series_specifics_exercise.md).


### Next unit
Proceed with [Temporal vs. spatial and spectral resolution](../05_specific_resolution_contribution/05_specific_resolution_contribution.md)


## References

### Key literature


### Further articles and referenced literature
