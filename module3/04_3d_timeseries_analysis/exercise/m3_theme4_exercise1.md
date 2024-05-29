# Exercise: Time series analysis of 3D point clouds

## Time series-based change analysis of surface dynamics at a sandy beach

In this exercise, you will perform time series-based surface change analysis on a time series of permanent TLS point clouds of the sandy beach at Kijkduin for a timespan of around 6 months ([Vos et al., 2022](#references)). See the introduction to the case study and dataset [here](../../../data_usecases/usecase_beach_kijkduin.md).

The objective is to assess surface dynamics with two methods: time series clustering (following [Kuschnerus et al., 2021](#references)) and 4D objects-by-change (following [Anders et al., 2021](#references)). Look into the related articles for comparison of possible surface dynamics at the site and help for deciding on suitable parameters, etc.

## Software and data
This exercise should be solved using Python with the [`py4dgeo`](https://github.com/3dgeo-heidelberg/py4dgeo) library. You can follow the workflow introduced in the [lesson of this theme](../04_3d_timeseries_analysis.ipynb). Also, make use of the software documentations!

Use [CloudCompare](../../../software/software_cloudcompare.md) or GIS Software (e.g., [QGIS](../../../software/software_qgis.md)) to check and visualize your results.

The dataset will be a subsampled version of the original time series, using 12-hourly epochs of point clouds and spatial subsampling to 50 cm. In the data directory `kijkduin`, you find the prepared input point clouds and a core points point cloud, which is manually cleaned from noise.

## Loading data and calculation of surface changes

Prepare the analysis by compiling the list of files (epochs) and read the timestamps from the file names (format `YYMMDD_hhmmss`) into `datetime` objects. Use the point cloud files and timestamps to create a py4dgeo `SpatiotemporalAnalysis` object. For this you need to instantiate the M3C2 algorithm. You can use the point cloud file `170115_150816_aoi_50cm.laz` as core points. Explore the point cloud properties in CloudCompare: 

* Considering the available point density and surface characteristics, what would be a suitable cylinder radius for the distance calculation?
* What would be a suitable approach to derive the surface normals in this topography and expected types of surface changes?

Hint: In this flat topography and predominant provess of sand deposition and erosion, it can be suitable to orient the normals purely vertically. In this case, they do not need to be computed, and you can [customize the py4dgeo algorithm](https://py4dgeo.readthedocs.io/en/latest/customization.html#Changing-search-directions) accordingly.

Use the first point cloud in the time series (list of files) as reference epoch. You can assume a registration error of 1.9 cm for the M3C2 distance calculation (cf. [Vos et al., 2022](#references)).

Explore the spatiotemporal change information by visualizing the changes at a selected epoch and visualizing the time series at a selected location.

## Temporal smoothing

You are dealing with a temporal subset of the original hourly time series. The effect of temporal measurement variability may therefore be less pronounced (compared to the assessment in, e.g., Anders et al., 2019). Nonetheless, you may apply temporal smoothing to reduce the influence of noise on your change analysis using a rolling median averaging of one week. This will also fill possible gaps in your data, e.g., lower ranges during poor atmospheric conditions or no data due to water coverage during tides on the lower beach part. 

Visualize the raw and smoothed change values in the time series of your selected location.

## Time series clustering
To derive characteristic change patterns on the sandy beach, perform k-means clustering of the time series following [Kuschnerus et al. (2021)](#references). Assess the clustering for different selections of `k` numbers of clusters.

* Can you interpret the characteristics of different parts on the beach? Visualize example time series for different clusters.
* From which number of clusters do you see a clear separation in overall units of the beach area?
* What are some detail change patterns that become visible for a higher number of clusters?

## Extraction of 4D objects-by-change

Now use the 4D objects-by-change (4D-OBC) method to identify individual surface activities in the beach scene. The objective is to extract temporary occurrences of accumulation or erosion, as occurs when a sand bar is formed during some timespan, or when sand is deposited by anthropogenic works. This type of surface activity is implemented with the original seed detection in py4dgeo, so you do not need to customize the algorithm. Decide for suitable parameters following [Anders et al. (2021)](#references) - but bear in mind that we are using a different temporal resolution, so you may need to adjust the temporal change detection.

Perform the extraction for selected seed locations, e.g. considering interesting clusters of change patterns identified in the previous step. In principle, the spatiotemporal segmentation can also be applied to the full dataset (all time series at all core point locations are used as potential seed candidates), but long processing time needs to be expected.

## Solution

Good job on finishing this exercise! You may take a look at the solution provided [here](m3_theme4_exercise1_solution1.ipynb).

We will not further go into the analysis here, but note that the 4D point clouds at this sandy beach are featured as a [research-oriented case study](../../06_casestudy_sandybeach/06_casestudy_sandybeach.ipynb)!

<a id='references'></a>
# References

* Anders, K., Lindenbergh, R. C., Vos, S. E., Mara, H., de Vries, S., & Höfle, B. (2019). High-Frequency 3D Geomorphic Observation Using Hourly Terrestrial Laser Scanning Data Of A Sandy Beach. ISPRS Ann. Photogramm. Remote Sens. Spatial Inf. Sci., IV-2/W5, pp. 317-324. doi: [10.5194/isprs-annals-IV-2-W5-317-2019](https://doi.org/10.5194/isprs-annals-IV-2-W5-317-2019).
* Anders, K., Winiwarter, L., Mara, H., Lindenbergh, R., Vos, S. E., & Höfle, B. (2021). Fully automatic spatiotemporal segmentation of 3D LiDAR time series for the extraction of natural surface changes. ISPRS Journal of Photogrammetry and Remote Sensing, 173, pp. 297-308. doi: [10.1016/j.isprsjprs.2021.01.015](https://doi.org/10.1016/j.isprsjprs.2021.01.015).
* Kuschnerus, M., Lindenbergh, R., & Vos, S. (2021). Coastal change patterns from time series clustering of permanent laser scan data. Earth Surface Dynamics, 9 (1), pp. 89-103. doi: [10.5194/esurf-9-89-2021](https://doi.org/10.5194/esurf-9-89-2021).
* Vos, S., Anders, K., Kuschnerus, M., Lindenberg, R., Höfle, B., Aarnikhof, S. & Vries, S. (2022). A high-resolution 4D terrestrial laser scan dataset of the Kijkduin beach-dune system, The Netherlands.  Scientific Data, 9:191. doi: [10.1038/s41597-022-01291-9](https://doi.org/10.1038/s41597-022-01291-9).

