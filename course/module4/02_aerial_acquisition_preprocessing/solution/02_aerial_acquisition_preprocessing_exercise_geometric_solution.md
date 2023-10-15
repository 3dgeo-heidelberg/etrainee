---
title: "E-TRAINEE: Subpixel classification - report"
description: "This is an example report for the geometric correction exercise within the second theme of the Airborne Imaging Spectroscopy Time Series Analysis module."
dateCreated: 2023-06-06
authors: Alex Srolleru
contributors:
estimatedTime:
---

## Report 


##### Data preparation, relative and absolute accuracy

Image data was ...

<div align="center"><i>"Raw" image data</i></div>

| "Raw" image data |           |                        |          |   |                      |           |                        |          |
|:-----------------:|:---------:|:----------------------:|:--------:|:---:|:--------------------:|:---------:|:----------------------:|:--------:|
| **Absolute accuracy** | shift [m] | standard deviation [m] | RMSE [m] |   | **Relative accuracy**    | shift [m] | standard deviation [m] | RMSE [m] |
| strip (line) 2    | 0.35      | 0.04                   | 0.35     |   | strip (line) 2 and 3 | 2.01      | 0.32                   | 2.03     |
| strip (line) 3    | 1.28      | 0.51                   | 1.71     |   | strip (line) 3 and 4 | 1.50      | 0.12                   | 1.50     |
| strip (line) 4    | 0.39      | 0.08                   | 0.40     |


##### Image registration

Georeferencing....

<p align="center">
<img src="media/affine_mosaic.jpg" title="Geometrically corrected hyperspectral image strips - affine transfromation" alt="Figure 1" width="600"/>
<div align="center"><i>Geometrically corrected hyperspectral image strips - affine transfromation</i></div>
<br>     
<p align="center">
<img src="media/spline_mosaic.jpg" title="Geometrically corrected hyperspectral image strips - spline transfromation" alt="Figure 1" width="600"/>
</p>
<div align="center"><i>Geometrically corrected hyperspectral image strips - spline transfromation</i></div>
<br>
The residuals on the GCPs were....

| GCP residuals  |                               |   |                       |
|:--------------:|:-----------------------------:|:---:|:---------------------:|
| **mean [m]**       | **1st polynomial transformation** |   | **spline transformation** |
| strip (line) 2 | 0.04                          |   | 0.00                  |
| strip (line) 3 | 0.03                          |   | 0.00                  |
| strip (line) 4 | 0.01                          |   | 0.00                  |

##### Accuracy assessment

Accuracy...

<div align="center"><i>1st polynomial transformation</i></div>

|                   |           |                        |          |   |                      |           |                        |          |
|:-----------------:|:---------:|:----------------------:|:--------:|:---:|:--------------------:|:---------:|:----------------------:|:--------:|
| **Absolute accuracy** | shift [m] | standard deviation [m] | RMSE [m] |   | **Relative accuracy**   | shift [m] | standard deviation [m] | RMSE [m] |
| strip (line) 2    | 0.08      | 0.05                   | 0.09     |   | strip (line) 2 and 3 | 0.13      | 0.08                   | 0.14     |
| strip (line) 3    | 0.06      | 0.03                   | 0.07     |   | strip (line) 3 and 4 | 0.12      | 0.08                   | 0.14     |
| strip (line) 4    | 0.04      | 0.02                   | 0.04     |

<div align="center"><i>Affine transformation</i></div>

|                   |           |                        |          |   |                      |           |                        |          |
|:-----------------:|:---------:|:----------------------:|:--------:|:---:|:--------------------:|:---------:|:----------------------:|:--------:|
| **Absolute accuracy** | shift [m] | standard deviation [m] | RMSE [m] |   | **Relative accuracy**    | shift [m] | standard deviation [m] | RMSE [m] |
| strip (line) 2    | 0.09      | 0.05                   | 0.11     |   | strip (line) 2 and 3 | 0.13      | 0.04                   | 0.14     |
| strip (line) 3    | 0.07      | 0.04                   | 0.08     |   | strip (line) 3 and 4 | 0.12      | 0.07                   | 0.13     |
| strip (line) 4    | 0.05      | 0.01                   | 0.06     |



##### Q&A 

* Evaluate the absolute and relative accuracy after geometric correction. What is the maximum error? Is the resulting accuracy sufficient?  
    + 
* Compare the “raw” image strips with the geometrically corrected (orthorectified) image strips in terms of computed accuracy and visual inspection.  
    + 
* Are there any differences between the results of the spline and polynomial transformations?  
    + 
* Comment on the used resampling method: what does “Nearest neighbour” ensure? Would using a different resampling type affect the image, and if yes, then how?  
    + 
### Back to theme 
Proceed by returning to [Aerial/RPAS hyperspectral data acquisition and pre-processing](../02_aerial_acquisition_preprocessing.md)
