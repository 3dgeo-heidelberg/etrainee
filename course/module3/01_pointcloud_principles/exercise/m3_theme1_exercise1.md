# Exercise: Principles of 3D/4D geographic point clouds

In this exercise, you will get familiar with 3D point clouds in open, graphical software. You will further visually explore multitemporal point clouds and assess changes using visual tools and manual measurements.

## Software and data

Use the software [CloudCompare](../../../software/software_cloudcompare.md) for this exercise. For help with the basic usage of CloudCompare, you may refer to the tutorial videos on the [CloudCompare](https://cloudcompare.org/) website or on this [workshop-website](http://cloudcompare.org/tutorials.html).

The dataset will be point clouds of a rock glacier acquired by UAV photogrammetry and laser scanning. See the introduction to the use case and dataset [here](../../../data_usecases/usecase_rockglacier_ahk.md).

Use the data from the directory `ahk` in the course data repository.

## Explore the point clouds
Load a UAV laser scanning point cloud of 2021 into CloudCompare. Look at both the photogrammetric and laser scanning point cloud, but use either to work on the following questions. Later on, you will compare them.

* How many points does the point cloud have? 
* What are the measures of the site (width and length of the bounding box)? 
* What is the approximate length of the acquired part of the rock glacier tongue (manual measurement)?
* How many attributes (_scalar field_ in CloudCompare) and which does the point cloud have? Note that attributes were removed to reduce the data volume of the course, so you may miss some typical LiDAR attributes.

Load the photogrammetric point cloud (`ahk_2021_photo.laz`) and compare:

* What are the different available attributes?
* How do the point clouds differ visually regarding point density and coverage?
* How does the representation of individual boulders on the rock glacier differ visually?

Prepare a visualization comparing both point clouds at the same close-up view of few boulders - either as two images or as an animation. Do not forget to add the basic elements of scale bar and axes orientation.

## Manual editing of the point cloud
Use the [`Segment`](https://cloudcompare.org/doc/wiki/index.php?title=Interactive_Segmentation_Tool) tool in CloudCompare to cut out individual boulders from the rock glacier point cloud. Then [`merge`](https://www.cloudcompare.org/doc/wiki/index.php/Merge) the individual boulders and have CloudCompare "add indexes of the original point clouds". This provides you (a part of) the point cloud with a point attribute of individual boulder indices - a manual boulder segmentation.

Load the file ULS point cloud from 2020 into your CloudCompare project (`ahk_2020_uls.laz`). Check the extract of your boulders or some local area visually, can you see any changes 2020 to 2021? 


* What challenges do you face when cutting out a boulder manually?
* Do you have an idea how boulder segmentation could be done automatically? Think of the features and decisions you would implement in an algorithm.

Share your result visually – make a nice image of your segmented boulders using some tricks CloudCompare’s visualization options. 
Some suggestions:

* Adjust the color of the background (e.g., white and no shading). Don’t forget to adjust the colors of the bounding box, labels, etc. then, too. 
* Color the boulders by single colors to make the segmentation nicely visible. 
* Use the GL Shader to make the geometry better visible and have a “plastic touch”. 
* Can you think of more?

Render the view to an image.

## Derivation of roughness
For the derivation of surface roughness, use the 2021 ULS point cloud. Cut out a subset of a small area covering part of the rock glacier and part of the adjacent area.

Calculate the surface roughness. As you know, roughness is scale-dependent. Can you find a suitable radius to (i) distinguish individual boulder faces, and to (ii) distinguish the rock glacier (composed of boulders) from the grass and rock areas next to the rock glacier tongue?

## Inspection of topographic change

Methods of change detection and quantification are covered by subsequent themes. However, you may already visually identify movement and deformation of the rock glacier body. Compare the 2020 and 2021 ULS point clouds of the rock glacier. 

Check changes of the rock glacier in the point clouds with the following approaches:
 
* Color each point cloud by single, distinct colors (e.g., blue and red).
* Examine a profile through both point clouds along the rock glacier tongue.
* Measure the distance from one point cloud to the corresponding surface of the other.

Is the change measurement straight-forward, can you be sure to measure the same surfaces, e.g., of corresponding boulders everywhere?

In which direction(s) do you measure change: vertically, horizontally, surface orientation, ...?

## Wrap up

Did you make it through the exercise? Discuss with peers and consider the [solution provided in the course](m3_theme1_exercise1_solution1.md).

You are now familiar with point cloud editing and analysis in a graphical user interface. Next, you should try to process point clouds using programming, e.g., with Python.

Further, you should now get into 3D change analysis of this complex natural phenomenon with the available multitemporal point cloud data!
