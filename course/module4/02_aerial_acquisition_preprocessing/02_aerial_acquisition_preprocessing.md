---
title: "E-TRAINEE: Aerial and RPAS hyperspectral data acquisition and image pre-processing workflow"
description: "This is the second theme within the Airborne Imaging Spectroscopy Time Series Analysis module."
dateCreated: 2021-03-28
authors:
contributors: 
estimatedTime: 
---

# Airborne hyperspectral data acquisition and pre-processing

Acquisition of airborne hyperspectral images requires careful flight planning supported by field campaigns. 

The following preprocessing of data comprises necessary radiometric and geometric correction. In addition, spectra transformations and filtering can be carried out to reduce data volume and suppress the noise present in the data.

## Objectives

In this theme, you will learn about 

* flight planning and in-situ measurements for radiometric and geometric correction of images,

* methods of radiometric correction of HS images,

* geometric correction,

* selected spectra transformations (e.g., minimum noise fraction, continuum removal, spectral indices), and spectra smoothening and denoising.

The theme includes an exercise, a self-evaluation quiz, and a list of references.


Acquisition of airborne hyperspectral images requires careful flight planning supported by field campaigns. 
The following preprocessing of data comprises necessary radiometric and geometric correction. In addition, spectra transformations and filtering can be carried out to reduce data volume and suppress the noise present in the data.

In the practical exercise you will carry out a geometric correction of images acquired with a Nano-Hyperspec® camera mounted on the DJI Matrice 600 Pro platform.
After finishing this theme, you will be aware of flight parameters settings and in-situ measurements to be considered for a successful HS flight mission, you will understand principles of radiometric and geometric corrections, and you will be familiar with noise and data volume reduction methods.

The content of the lesson is curently available as a [pdf file](M4_T2_Intro.pdf).

## Self-evaluation quiz

<form name="quiz" action="" method="post" onsubmit="evaluate_quiz(); return false">

<!--Question 1-->
<label for="q_01">
When planning a flight mission,
</label><br>
<input type="checkbox" name="q_01">no overlap between image lines/strips is necessary.<br>
<input type="checkbox" name="q_01">overlap is necessary only in the hilly terrain.<br>
<input type="checkbox" name="q_01">a higher value of overlap is better in hilly terrain than in flat terrain.<br>
<div hidden id="correct_q_01">a higher value of overlap is better in hilly terrain than in flat terrain.</div>
<output id="output_q_01"></output><br><br>

<!--Question 2-->
<label for="q_02">
If possible, how would you choose the flight azimuth?
</label><br>
<input type="checkbox" name="q_02">Perpendicular to the current sun azimuth.<br>
<input type="checkbox" name="q_02">Close to the current sun azimuth.<br>
<input type="checkbox" name="q_02">Arbitrary. The relations between the azimuths does not influence the image radiometry.<br>
<div hidden id="correct_q_02">Close to the current sun azimuth.</div>
<output id="output_q_02"></output><br><br>

<!--Question 3-->
<label for="q_03">
You have a camera with a focal length of 15 mm and a pixel size of 7.5 μm. What flying height above the terrain do you need to plan to achieve the GSD of 5 cm?
</label><br>
<input type="checkbox" name="q_03">70 m<br>
<input type="checkbox" name="q_03">85 m<br>
<input type="checkbox" name="q_03">100 m<br>
<div hidden id="correct_q_03">100 m</div>
<output id="output_q_03"></output><br><br>

<!--Question 4-->
<label for="q_04">
Radiometric correction includes:
</label><br>
<input type="checkbox" name="q_04">sensor calibration and atmospheric correction.<br>
<input type="checkbox" name="q_04">sensor calibration.<br>
<input type="checkbox" name="q_04">atmospheric correction.<br>
<div hidden id="correct_q_04">sensor calibration and atmospheric correction.</div>
<output id="output_q_04"></output><br><br>

<!--Question 5-->
<label for="q_05">
Which are empirical methods for atmospheric correction?
</label><br>
<input type="checkbox" name="q_05">Empirical line and radiative transfer model.<br>
<input type="checkbox" name="q_05">Empirical line and dark object subtraction.<br>
<input type="checkbox" name="q_05">Dark object subtraction and radiative transfer model.<br>
<div hidden id="correct_q_05">Empirical line and dark object subtraction.</div>
<output id="output_q_05"></output><br><br>

<!--Question 6-->
<label for="q_06">
The platform is equipped with a GNSS/INS. At the same time 2 GCPs were measured. What kind of georeferencing can you carry out?
</label><br>
<input type="checkbox" name="q_06">Direct georeferencing<br>
<input type="checkbox" name="q_06">Integrated sensor orientation<br>
<input type="checkbox" name="q_06">Indirect georeferencing<br>
<div hidden id="correct_q_06">Direct georeferencing&Integrated sensor orientation</div>
<output id="output_q_06"></output><br><br>

<input type="submit" value="Submit" style="font-size:14pt"><br><br>

<output id="output_overall">
</output>
</form>

## Exercise

### Geometric correction

The aim of this exercise is to perform geometric correction of hyperspectral image data acquired with an UAV pushbroom scanner.  

Please proceed to the exercise: [Geometric correction](02_aerial_acquisition_preprocessing_exercise_geometric.md).

### Spectra smoothening and denoising 

Please proceed to the tutorial: [Spectra smoothening and denoising](filtering_spectral_curve.ipynb).

### Next unit
Proceed with [In situ and laboratory spectroscopy of vegetation](../03_relating_imagery_lab_vegetation/03_01_optical_parameters_of_foliage.md)


## References

### Key literature

Pepe, M., Fregonese, L., Scaioni, M. (2018). Planning airborne photogrammetry and remote-sensing missions with modern platforms and sensors. European Journal of Remote Sensing, 51(1), 412-436. https://doi.org/10.1080/22797254.2018.1444945

Schläpfer, D., Richter, R., Hueni, A. (2009). Recent developments in operational atmospheric and radiometric correction of hyperspectral imagery. In Proc. 6th EARSeL SIG IS Workshop (pp. 16-19). https://www.researchgate.net/publication/279261110_Recent_developments_in_operational_atmospheric_and_radiometric_correction_of_hyperspectral_imagery

Habib, A., Han, Y., Xiong, W., He, F., Zhang, Z., Crawford, M. (2016). Automated ortho-rectification of UAV-based hyperspectral data over an agricultural field using frame RGB imagery. Remote Sensing, 8(10), 796. https://doi.org/10.3390/rs8100796  

### Further articles, referenced literature and resources
Angel, Y., Turner, D., Parkes, S., Malbeteau, Y., Lucieer, A., McCabe, M. F. (2019). Automated georectification and mosaicking of UAV-based hyperspectral imagery from push-broom sensors. Remote Sensing, 12(1), 34. https://doi.org/10.3390/rs12010034 

ATCOR-4 (2023): ATCOR 4 - for Airborne Remote Sensing Systems. https://www.rese-apps.com/software/atcor-4-airborne/index.html 

Baugh, W. M., Groeneveld, D. P. (2008). Empirical proof of the empirical line. International Journal of Remote Sensing, 29(3), 665-672. https://doi.org/10.1080/01431160701352162

Broge, N. H., & Mortensen, J. V. (2002). Deriving green crop area index and canopy chlorophyll density of winter wheat from spectral reflectance data. Remote sensing of environment, 81(1), 45-57. https://doi.org/10.1016/S0034-4257(01)00332-7 

Canada Centre for Mapping and Earth Observation – Remote Sensing Tutorial. https://natural-resources.canada.ca/maps-tools-and-publications/satellite-imagery-and-air-photos/tutorial-fundamentals-remote-sensing/9309

Albrechtová, J., Kupková, L., Campbell, P. K. (2017). Metody hodnocení fyziologického stavu smrkových porostů: případové studie sledování vývoje stavu smrkových porostů v Krušných horách v letech 1998-2013. Česká geografická společnost. 

Červená, L., Lysák, J., Potůčková, M., Kupková, L. (2020). Zkušenosti se zpracováním hyperspektrálních dat pořízených UAV. GIS Ostrava. https://doi.org/10.31490/9788024843988-4 

Colomina, I., Molina, P. (2014). Unmanned aerial systems for photogrammetry and remote sensing: a review. ISPRS J. Photogramm. Remote Sens. 92, 79–97 https://doi.org/10.1016/j.isprsjprs.2014.02.013 

ENVI (2023). Vegetation Indices Background. https://www.nv5geospatialsoftware.com/docs/backgroundvegetationindices.html 

Förstner, W., Wrobel, B. P. (2016). Photogrammetric computer vision. Springer International Publishing Switzerland.

Green, A. A., Berman, M., Switzer, P., & Craig, M. D. (1988). A transformation for ordering multispectral data in terms of image quality with implications for noise removal. IEEE Transactions on geoscience and remote sensing, 26(1), 65-74. DOI: 10.1109/36.3001

Hadley, B. C., Garcia-Quijano, M., Jensen, J. R., Tullis, J. A. (2005). Empirical versus model‐based atmospheric correction of digital airborne imaging spectrometer hyperspectral data. Geocarto International, 20(4), 21-28. https://doi.org/10.1080/10106040508542360

Hakala, T. et al. (2018). Direct reflectance measurements from drones: Sensor absolute radiometric calibration and system tests for forest reflectance characterization. Sensors, 18(5), 1417. https://doi.org/10.3390/s18051417 

Hanuš, J., Fabiánek, T., Fajmon, L. (2016). Potential of airborne imaging spectroscopy at CzechGlobe. The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, 41, 15-17. https://doi.org/10.5194/isprs-archives-XLI-B1-15-2016 

Hruska, R., Mitchell, J., Anderson, M., Glenn, N. F. (2012): Radiometric and Geometric Analysis of Hyperspectral Imagery Acquired from an Unmanned Aerial Vehicle. Remote Sensing. 9, 4, 2736–2752. https://doi.org/10.3390/rs4092736 

Jiang, S., Jiang, C., Jiang, W. (2020). Efficient structure from motion for large-scale UAV images: A review and a comparison of SfM tools. ISPRS Journal of Photogrammetry and Remote Sensing, 167, 230-251. https://doi.org/10.1016/j.isprsjprs.2020.04.016 

Kokaly, R. F., Clark, R. N. (1999). Spectroscopic determination of leaf biochemistry using band-depth analysis of absorption features and stepwise multiple linear regression. Remote sensing of environment, 67(3), 267-287. https://doi.org/10.1016/S0034-4257(98)00084-4 

Kraus, K. (2007).  Photogrammetry: Geometry from Images and Laser Scans. de Gryter, 2nd edition.

Malenovsky, Z., Ufer, C., Lhotáková, Z., Clevers, J. G., Schaepman, M. E., Albrechtová, J., & Cudlín, P. (2006). A new hyperspectral index for chlorophyll estimation of a forest canopy: Area under curve normalised to maximal band depth between 650-725 nm. EARSeL eProceedings, 5(2), 161-172. https://library.wur.nl/WebQuery/wurpubs/346566 

Merzah, Z. F.,  Jaber, H. S. (2020). Assessment of Atmospheric Correction Methods for Hyperspectral Remote Sensing Imagery Using Geospatial Techniques. In IOP Conference Series: Materials Science and Engineering (Vol. 745, No. 1, p. 012123). IOP Publishing. https://iopscience.iop.org/article/10.1088/1757-899X/745/1/012123

de Miguel, E., Jiménez, M., Pérez, I., de la CÁMARA, Ó. G., Muñoz, F., Gómez-Sánchez, J. A. (2015). AHS and CASI processing for the REFLEX remote sensing campaign: methods and results. Acta Geophysica, 63, 1485-1498. https://doi.org/10.1515/acgeo-2015-0031 

Ortiz, J. D., Avouris, D., Schiller, S., Luvall, J. C., Lekki, J. D., Tokars, R. P., Becker, R. (2017). Intercomparison of approaches to the empirical line method for vicarious hyperspectral reflectance calibration. Frontiers in Marine Science, 4, 296. https://doi.org/10.3389/fmars.2017.00296 

Remondino, F., Spera, M. G., Nocerino, E., Menna, F., Nex, F. (2014). State of the art in high density image matching. The photogrammetric record, 29(146), 144-166. https://doi.org/10.1111/phor.12063

Richter, R. (1997). Correction of atmospheric and topographic effects for high spatial resolution satellite imagery. International journal of remote sensing, 18(5), 1099-1111. https://doi.org/10.1080/014311697218593

Richter, R., Schläpfer, D. (2002). Geo-atmospheric processing of airborne imaging spectrometry data. Part 2: Atmospheric/topographic correction. International Journal of Remote Sensing, 23(13), 2631-2649. https://doi.org/10.1080/01431160110115834 

Roberts, D. A., Roth, K. L., Wetherley, E. B., Meerdink, S. K., Perroy, R. L. (2018). Hyperspectral vegetation indices. In Hyperspectral indices and image classifications for agriculture and vegetation (pp. 3-26). CRC press. 

Schläpfer, D., Popp, C., Richter, R. (2020). Drone data atmospheric correction concept for multi-and hyperspectral imagery–the DROACOR model. Int. Arch. Photogramm. Remote Sens. Spatial Inf. Sci., XLIII-B3-2020, 473–478. https://doi.org/10.5194/isprs-archives-XLIII-B3-2020-473-2020 

Schowengerdt, R. A. (2006). Remote sensing: models and methods for image processing. Elsevier, 3rd edition.

Stull, R. (2023): Scattering. LibreTexts, Geosciences. 22.4 Scattering. https://geo.libretexts.org/Bookshelves/Meteorology_and_Climate_Science/Practical_Meteorology_%28Stull%29/22%3A_Atmospheric_Optics/22.03%3A_New_Page

Suomalainen, J., Anders, N., Iqbal, S., Roerink, G., Franke, J., Wenting, P., ... , Kooistra, L. (2014). A lightweight hyperspectral mapping system and photogrammetric processing chain for unmanned aerial vehicles. Remote Sensing, 6(11), 11013-11030. https://doi.org/10.3390/rs61111013 

Suomalainen, J., Oliveira, R. A., Hakala, T., Koivumäki, N., Markelin, L., Näsi, R., Honkavaara, E. (2021). Direct reflectance transformation methodology for drone-based hyperspectral imaging. Remote Sensing of Environment, 266, 112691. https://doi.org/10.1016/j.rse.2021.112691 

Toth, C., Józków, G. (2016). Remote sensing platforms and sensors: A survey. ISPRS Journal of Photogrammetry and Remote Sensing, 115 (2016) 22–36. doi: https://doi.org/10.1016/j.isprsjprs.2015.10.004

Turner, D., Lucieer, A., McCabe, M., Parkes, S., Clarke, I. (2017). Pushbroom hyperspectral imaging from an unmanned aircraft system (uas)–geometric processing workflow and accuracy assessment. The International Archives of the Photogrammetry. Remote Sensing and Spatial Information Sciences. XLII-2/W6. 379–384. http://dx.doi.org/10.5194/isprs-archives-xlii-2-w6-379-2017 

Vaiphasa, C. (2006). Consideration of smoothing techniques for hyperspectral remote sensing. ISPRS journal of photogrammetry and remote sensing, 60(2), 91-99. https://doi.org/10.1016/j.isprsjprs.2005.11.002 

Vermote, E. F., Tanré, D., Deuze, J. L., Herman, M., Morcette, J. J. (1997). Second simulation of the satellite signal in the solar spectrum, 6S: An overview. IEEE transactions on geoscience and remote sensing, 35(3), 675-686. DOI: 10.1109/36.581987 

Zhou, Q., Wang, S., Liu, N., Townsend, P. A., Jiang, C., Peng, B., Verhoef, W., Guan, K. (2023). Towards operational atmospheric correction of airborne hyperspectral imaging spectroscopy: Algorithm evaluation, key parameter analysis, and machine learning emulators. ISPRS Journal of Photogrammetry and Remote Sensing, 196, 386-401. https://doi.org/10.1016/j.isprsjprs.2022.11.016 
