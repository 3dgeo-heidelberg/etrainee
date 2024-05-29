# Exercise: Principles and basic algorithms of 3D change detection and analysis

## 3D Change Analysis at an Active Rock Glacier using Multitemporal Point Clouds

In this exercise, you will perform a surface change analysis on TLS point clouds of the Äußeres Hochebenkar rock glacier (46°50’11''N, 11°00’20‘’E) for two consecutive years. See the introduction to the case study and dataset [here](../../../data_usecases/usecase_rockglacier_ahk.md).

The objective is to perform a full workflow of 3D change analysis with

* Assessment of alignment uncertainty
* Change analysis using the M3C2 algorithm 
* Change representation and assessment of results
* For the fast ones: Comparison to change analysis via DEM differencing

Look into the article by [Zahs et al., 2019](https://doi.org/10.1002/ppp.2004) for comparison of possible surface dynamics at the site and help for deciding on suitable parameters, etc.

## Software and data
This exercise can be solved fully in [CloudCompare](../../../software/software_cloudcompare.md) or using Python with the [`py4dgeo`](https://github.com/3dgeo-heidelberg/py4dgeo) library. If you have the Python skills, we recommend to work on the exercise with Python in a Jupyter notebook, hence obtaining a sharable and reproducible workflow.

Use CloudCompare and GIS Software (e.g., [QGIS](../../../software/software_qgis.md)) to check and visualize your results.

In any case, make use of the software documentations!

The dataset will be two epochs of point clouds acquired by UAV laser scanning in 2020 and 2021: `ahk_2020_uls.laz` and `ahk_2021_uls.laz`.

## Assessment of alignment uncertainty
The epochs are georeferenced, i.e., multitemporal point clouds are registered in a common coordinate reference frame. The point clouds have further been fine aligned using an ICP method on stable parts outside the rock glacier area. You may assume that the best possible alignment between the multitemporal data has been achieved.

For change analysis, it is important to assess the uncertainty of the point cloud alignment for information on the minimum detectable change. Do this, by cutting out some stable rock surfaces outside the rock glacier and checking the cloud-to-cloud distances for these subsets. You may cut out point cloud subsets manually in CloudCompare, or define polygons (e.g., in QGIS) to extract the parts from the full point cloud in the Python workflow.

## 3D change analysis via point cloud distance computation

Calculate the distance between point clouds of the two epochs using the M3C2 algorithm [Lague et al., 2013](https://doi.org/10.1016/j.isprsjprs.2013.04.009). 

Think about a suitable parametrization:
* Normal scale D: diameter of point neighborhood to use for normal vector computation. *Hint*: Aim for overall, larger-scale surface change, e.g. due to rock glacier creep or heave/thaw (instead of individual boulders).
* Projection scale d: diameter of cylindrical point neighborhood to obtain average position.
* Maximum cylinder depth: Maximum distance along normal at which to obtain distances to the other point cloud.
* Preferred normal orientation.
* Registration error ~ alignment accuracy

Consider using the [CloudCompare Wiki](https://www.cloudcompare.org/doc/wiki/index.php?title=M3C2_(plugin)) and [py4dgeo documentation](https://py4dgeo.readthedocs.io/en/latest/intro.html).


## Change representation and assessment of results

Visualize the obtained point cloud distances and corresponding information layers, such as the level of detection and the normal vectors representing the direction of changes.

Prepare the result assessment for interpretation by analysts. For example, you may rasterize the different layers and create a map, e.g., of the derived surface changes in GIS software. Tip: Use the Web Map Service (WMS) of Tyrol as a basemap: [https://gis.tirol.gv.at/arcgis/services/Service_Public/orthofoto/MapServer/WMSServer?](https://gis.tirol.gv.at/arcgis/services/Service_Public/orthofoto/MapServer/WMSServer?), which can be implemented in QGIS (Layer > add Layer > add WMS/WMTS Layer).


What are the different properties of visible changes and to which types of surface activity would you attribute them? Think of heave and subsidence processes, individual boulder movement, and rock glacier creep (cf. [Zahs et al., 2019](#references)).


## For the fast ones: Change analysis via DEM differencing

Generate a DEM from the point cloud of each epoch and subsequently difference them. Think about a suitable parametrization, particularly the interpolation method and neighborhood definition. Visualize the raster of change information in GIS software.

Compare the DEM of difference values to the M3C2 distances and their directions. Where do you see differences and how does the analysis hence benefit from a full 3D method of change quantification?

## Solution

This Exercise can be solved with Python or in CloudCompare. Find the solution for the Python approach [here](m3_theme3_exercise1_solution1.ipynb) and for the CloudCompare/QGIS approach [here](m3_theme3_exercise1_solution2.md).


## References

* Lague, D., Brodu, N., & Leroux, J. (2013). Accurate 3D comparison of complex topography with terrestrial laser scanner: Application to the Rangitikei canyon (N-Z). ISPRS Journal of Photogrammetry and Remote Sensing, 82, pp. 10-26. doi: [10.1016/j.isprsjprs.2013.04.009](https://doi.org/10.1016/j.isprsjprs.2013.04.009).

* Zahs, V., Hämmerle, M., Anders, K., Hecht, S., Sailer, R., Rutzinger, M., Williams, J. G., & Höfle, B. (2019). Multi-temporal 3D point cloud-based quantification and analysis of geomorphological activity at an alpine rock glacier using airborne and terrestrial LiDAR. Permafrost and Periglacial Processes, 30 (3), pp. 222-238. doi: [10.1002/ppp.2004](https://doi.org/10.1002/ppp.2004).

