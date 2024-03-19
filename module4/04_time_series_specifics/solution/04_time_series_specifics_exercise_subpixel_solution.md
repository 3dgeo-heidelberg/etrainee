---
title: "E-TRAINEE: Subpixel classification - report"
description: "This is an example report for the subpixel classification exercise within the Airborne Imaging Spectroscopy Time Series Analysis module."
dateCreated: 2023-02-18
authors: Alex Srolleru
contributors:
estimatedTime:
---

## Report
The hyperspectral image was loaded in the EnMAP-Box environment and visualized in true colors using the recommended bands. From the image metadata the following information was extracted: 

number of bands: 54  
wavelength range: 397.663 to 1001.839 nanometers  
spatial resolution: 0.09 m

Overlaying the image with the training polygons gives a clear overview of the location of the dominant grass stands. The mol species corresponds to the green polygons, the cv species to red, and the nard species is in violet. 

<p align="center">
<img src="media/01_polygon_overlay.jpg" title="Hyperspectral image in true colors overlaid with training polygons" alt="Figure 1" width="500"/>
</p>

<div align="center">

<i>Hyperspectral image in true colors overlaid with training polygons</i>
</div>

##### Endmember extraction

One endmember spectra for each species was extracted using the pixel purity index image. Pixels with the highest purity lying inside the training polygons were chosen. When compared to the provided semi-automatically pre-extracted endmembers, the reflectance values are generally lower in the longer wavelengths, however, the shape/trend of the curve remains the same. 

<p align="center">
<img src="media/02_spectral_library.png" title="Created spectral library" alt="Figure 2" width="600"/>
</p>

<div align="center">

<i>Created spectral library</i>
</div>

<p align="center">
<img src="media/03_mol_cv_nard_spectra.png" title="Comparison of the extracted endmember spectra (yellow) with the semi-automatically pre-extracted endmembers (white)" alt="Figure 3" width="500"/>
</p>

<div align="center">

<i>Comparison of the extracted endmember spectra (yellow) with the semi-automatically pre-extracted endmembers (white)</i>
</div>

##### Spectral unmixing

Spectral unmixing was carried out  on the hyperspectral image using the provided spectral library. The “Regressor” algorithm RandomForestRegressor was chosen to observe the effect of the “Number of mixtures per class” parameter. Values 100, 500, and 1000 were tested sequentially. All the other parameters were left at their defaults. Changing the value had a significant effect on the class fraction layer. A low mixture per class value favored the cv species, while a higher value favored the mol species. Increasing the amount also resulted in a less noisy image and more compact areas.

<p align="center">
<img src="media/04_mixtures.png" title="Effect of changing parameter Number of mixtures per class" alt="Figure 4" width="1600"/>
</p>

<div align="center">

<i>Effect of changing parameter Number of mixtures per class (Left: 100; Center: 500; Right: 1000)</i>
</div>

Setting the “Regressor” algorithm to LinearSVR and leaving all the other parameters at their default state gave the following results:

<p align="center">
<img src="media/05_class_layer.jpg" title="Class fraction layer and classification layer" alt="Figure 5" width="1000"/>
</p>

<div align="center">

<i>Class fraction layer and classification layer (Red: cv; Green: mol; Blue: nard)</i>
</div>

<p align="center">
<img src="media/06_single_band.jpg" title="Single band visualization (Left: cv; Center: mol; Right: nard)" alt="Figure 6" width="1600"/>
</p>

<div align="center">

<i>Single band visualization</i>
</div>

##### Q&A
* What does the class fraction layer represent? Describe the resulting RGB image, are there mixed/pure pixels?  
    + the class fraction layer represents the fraction/probability of the classes in  pixels; each image band corresponds to one species and holds the value of the fraction
one can distinguish compact areas with relatively pure pixels of cv (bright red), compact areas of mol mixed with cv (bright red and green), and mixed nard forming the “background”
* The northwest edges of compact mol areas seem to be mixed with cv, but not the other edges. Can you determine what is causing this effect?
    + shadows in the image
* The reference map contains the class desch which we did not classify. How are these areas manifested in the class fraction layer and the classification layer? 
    + class fraction layer: mixed species areas where none of the species is dominant 
    + classification layer: nard species
* Compare the classification layer and reference map. Do both maps show a good agreement in terms of spatial patterns? Discuss all the possible effects on the outcome.
    + spatial patterns yes - otherwise not so much
    + effects: data acquisition, geometric and radiometric corrections, endmember extraction, chosen mixing parameters and regression algorithm 
* What kind of data might be more suitable for subpixel classification and why? 
    + data with lower spatial resolution
    + more separable classes (spectrally distinct)

### Back to theme
Proceed by returning to [Machine learning in imaging spectroscopy](../04_time_series_specifics.md)
