---
title: "E-TRAINEE Module 2 Theme 4: Multitemporal classification - Exercise"
description: "This is the exercise in the fourth theme within the Satellite Multispectral Images Time Series Analysis module."
dateCreated: 2023-04-11
authors: "Krzysztof Gryguc, Adrian Ochtyra"
contributors: "Adriana Marcinkowska-Ochtyra"
estimatedTime: "1.5 hours"
output: 
  github_document:
    pandoc_args: "--wrap=none"
---

E-TRAINEE Module 2 Theme 4: Multitemporal classification - Exercise
================

# Exercise - Multitemporal classification of land cover in Karkonosze Mountains region

In this exercise you will be able to test the competences acquired in the Theme 4 theoretical part regarding the multitemporal classification. You will use a multitemporal Sentinel-2 dataset to perform Random Forest classification. After completing the necessary steps you will be able to compare the results acquired with different sets of input data and assess accuraccy achieved for different classes.

The main objective of this exercise is to show one of many approaches you can take when performing multitemporal satellite image classification. Based on the processes learned here, you will be able to apply the methods you have learned to different types of input data, algorithms, and accuracy evaluation methods.

## Basic preparation

### Prerequisites

For this exercise you will need the following software, data and tools:

- Software
  - R with RStudio (additional libraries required: `rgdal`, `raster`, `caret`, `randomForest`). You can access environment setup tutorial for the whole Module 2 here: -insert link to environment setup tutorial-
- Data
  - Downloaded data provided in the folder -link-

### Data

#### Imagery data

The imagery provided for this exercise consists of Sentinel-2 satellite imagery. The process of data preparation is described in the [Module 2 Theme 3 exercise Pipeline 1](#).

#### Reference data

**UNDER CONSTRUCTION. COMING SOON**

## Environment preparation

To start with, we want to load necessary libraries and data and set up some initial variables, which we will use further down the line.

Firstly, load required libraries into the environment: *rgdal*, *raster*, *caret*, *kernlab*, *randomForest*.

``` r
library(rgdal) # vector layer operations
library(raster) # raster processing
library(caret) # training/test layers preparation
library(randomForest) # RF model preparation
```

## Loading data

Now we can load required data into the RStudio environment. We will start with loading image data and vector reference layer.

``` r
reference <- readOGR("data_exercise/reference_50samples_per_class.shp", "reference_50samples_per_class") # reference vector data
image <- brick("data_exercise/S2_2022_classification_ready.tif") # RasterBrick with all the available bands
```

The bands in the raster bricks are ordered by date: first 11 bands (10 spectral bands + NDVI) are from the first term of acquisition (2022-06-19) and then the other terms follow.

The reference data consist of 450 polygons, 50 per each of 9 classes. You can see the overview of both image and reference data with these commands.

``` r
image
head(reference)
```

    > image
    class      : RasterBrick 
    dimensions : 1687, 2459, 4148333, 66  (nrow, ncol, ncell, nlayers)
    resolution : 10, 10  (x, y)
    extent     : 534440, 559030, 5619440, 5636310  (xmin, xmax, ymin, ymax)
    crs        : +proj=utm +zone=33 +datum=WGS84 +units=m +no_defs 
    source     : S2_2022_classification_ready.tif 
    names      : X2022_06_19_B2, X2022_06_19_B3, X2022_06_19_B4, X2022_06_19_B5, X2022_06_19_B6, X2022_06_19_B7, X2022_06_19_B8, X2022_06_19_B8A, X2022_06_19_B11, X2022_06_19_B12, X2022_06_19_NDVI, X2022_06_24_B2, X2022_06_24_B3, X2022_06_24_B4, X2022_06_24_B5, ... 

    > head(reference)
       fid     id Code_18             class local_id reference uwagi
    0 2196 309855     312 coniferous forest        1       yes  <NA>
    1 2319 307119     312 coniferous forest        2       yes  <NA>
    2 4822 290736     312 coniferous forest        3       yes  <NA>
    3 5123 290859     312 coniferous forest        4       yes  <NA>
    4 5436 288216     312 coniferous forest        5       yes  <NA>
    5 5697 285831     312 coniferous forest        6       yes  <NA>

## Pixel values extraction

Now that we have the data loaded we want to extract all the image values for each of the reference polygons. Each one of them covers 9 10x10 m pixels. In summary there will be 4050 samples to be used in training and validation data after the extraction.

The `extract_pixel_values` function will accept 4 arguments:

- `image` - variable containing image data
- `reference` - variable containing vector reference polygons
- `class_field_name` - name of the column in the `reference` containing class names
- `local_id` - name of the column in the `reference` containing id values

``` r
extract_pixel_values <- function(image, reference, class_field_name, local_id){
  
  counter <- 1 # a variable to keep track of the progress
  
  num_polygons <- nrow(reference@data) # the number of reference polygons
  extracted_data <- data.frame() # empty data frame for storing the results of the function
  
  class_column_index <- which(names(reference@data) == class_field_name) # index of the column containing class names
  id <- which(names(reference@data) == class_field_name) # index of the column containing id numbers
  
  for (poly_ind in seq(num_polygons)) { # loop; for each polygon in the set
    poly <- reference@polygons[poly_ind] # get the next polygon
    class <- reference@data[poly_ind, class_column_index] # get the class name of the polygon
    spatial_poly <- SpatialPolygons(poly) # make the polygon a SpatialPolygons object
    poly_px_vals <- extract(image, spatial_poly, df = TRUE) # extract the values of pixels
    poly_px_vals <- cbind(poly_px_vals[, 2: ncol(poly_px_vals)], class, poly_ind) # add class names and polygon index to the extracted values
    extracted_data <- rbind(extracted_data, poly_px_vals) # add the extracted values with additional information to the aggregate table
    
    
    print(paste0(round((counter / num_polygons) * 100, 1), "%")) # print the progress percentage
    counter <- counter + 1 # keep track of the progress
  }
  
  return(extracted_data) # return data frame containing all of the extracted values with class and local index values
}
```

Now apply the function to the data we have and save it to the `pixel_reference` variable.

``` r
pixel_reference <- extract_pixel_values(image, reference, "class", "local_id")
```

Save the extracted data frame to the external file in case you need to reload it, so you don’t have to wait for the extraction process to complete.

``` r
saveRDS(pixel_reference, file = "pixel_reference_exercise.RDS")

# in case you need to load it use the command below
# pixel_reference <- readRDS("pixel_reference_exercise.RDS")
```

## Classification scenario 1: the whole dataset

### Training/validation data preparation

Now that we have the reference dataset ready we can begin the classification scenario. First of all we want to divide the whole dataset into training and validation dataset. By running the commands below we can check how many samples of each class we have and how many reference polygons there are for each class.

``` r
table(pixel_reference$class)
table(reference@data$class)
```

    > table(pixel_reference$class)

    broad-leaved forest       built-up area   coniferous forest              fields             meadows  natural grasslands               rocks 
                    450                 450                 450                 450                 450                 450                 450 
                  scrub               water 
                    450                 450 


    > table(reference@data$class)

    broad-leaved forest       built-up area   coniferous forest              fields             meadows  natural grasslands               rocks 
                     50                  50                  50                  50                  50                  50                  50 
                  scrub               water 
                     50                  50 
    > 

To ensure reproducibility of partitioning we will set seed.

``` r
set.seed(14)
```

The partitioning will consist of two steps. First of all we will randomly choose 50% of polygons from each class and save their position number to `trainIndex` variable. Then this variable will be used to extract corresponding values by `poly_ind` column from `pixel_reference` table.

``` r
trainIndex <- createDataPartition(reference@data$class, p = 0.5, list = FALSE)

trainData <- pixel_reference[ pixel_reference$poly_ind %in% trainIndex, ]
valData <- pixel_reference[ !(pixel_reference$poly_ind %in% trainIndex), ]
```

Now we should have two sets of equal number of reference values for each class.

``` r
table(trainData$class)
table(valData$class)
```

    > table(trainData$class)

    broad-leaved forest       built-up area   coniferous forest              fields             meadows  natural grasslands               rocks 
                    225                 225                 225                 225                 225                 225                 225 
                  scrub               water 
                    225                 225 
                    
    > table(valData$class)

    broad-leaved forest       built-up area   coniferous forest              fields             meadows  natural grasslands               rocks 
                    225                 225                 225                 225                 225                 225                 225 
                  scrub               water 
                    225                 225 

### Parameters tuning

In order to achieve a satisfying result we want to tune the model parameters. One of the Random Forest algorithm parameter is ***mtry***, which is the number of random variables used in each tree. To find the number, which should yield the highest accuracy numbers we will use `tuneRF` function from the `randomForest` package.

The function takes several arguments:

- `x` (first argument) - matrix or data frame of predictor variables;
- `y` (second argument) - response vector (factor for classification);
- `ntreeTry` - number of trees used at the tuning step;
- `improve` - the (relative) improvement in OOB error must be by this much for the search to continue;
- `stepFactor` - at each iteration, mtry is inflated (or deflated) by this value.

We will again set seed and save the results of the fucntion to `tune` variable.

``` r
set.seed(14)

tune <- tuneRF(trainData[,1:66], 
               as.factor(trainData$class),
               ntreeTry = 500,
               improve = 0.001,
               stepFactor = 1.2)

tune
```

    > tune
           mtry    OOBError
    5.OOB     5 0.004938272
    6.OOB     6 0.003456790
    7.OOB     7 0.004444444
    8.OOB     8 0.004938272
    9.OOB     9 0.002962963
    10.OOB   10 0.003456790

<center>

<img src="media_exercise/mtry_tuning.png" title="mtry tuning" alt="mtry tuning" width="600"/>

<i>mtry parameter tuning.</i>
</center>

The lowest OOBError values were achieved `mtry` value of 9. In theory the higher the value the stronger the model, although high `mtry` values can also increase the correlation among the variables chosen for the split. In this case we will not test different values and set `mtry` parameter in the model as 9 given it’s lowest error.

### Model

The next step after tuning the parameters is a classification model development. There is a `randomForest` function inside the package of the same name, which is the implementation of the original RF algorithm. These are the arguments, which the function accepts used in the following code snippet:

- `x` (first argument) - a data frame or a matrix of predictors (from `trainData` variable);
- `y` (second argument) - response vector (factor for classification);
- `ntree` - number of trees used to produce the final model; 500 is empirically tested to usually yield satisfactory results;
- `mtry` - number of variables randomly sampled as candidates at each split (tuned in the previous step);
- `importance` - boolean, whether the model should store variable importance (needed to produce the plots);
- `do.trace` - helps to keep track of the modelling progress.

``` r
model_rf <- randomForest(trainData[ , 1:length(image@data@names)], as.factor(trainData$class), 
                         ntree = 500,
                         mtry = 9, 
                         importance = TRUE,
                         do.trace = 50)
```

To be able to access the model later it is recommended to save it locally.

    save(model_rf, file = "model_rf")

### Accuracy assessment

If we access the variable `model_rf` we will see the basic model information and confusion matrix calculated for the training data.

    > model_rf

    Call:
     randomForest(
     x = trainData[, 1:length(image@data@names)], 
     y = as.factor(trainData$class), 
     ntree = 500, 
     mtry = 9, 
     importance = TRUE, 
     do.trace = 50) 
     
     
                   Type of random forest: classification
                         Number of trees: 500
                         
    No. of variables tried at each split: 9

            OOB estimate of  error rate: 0.44%
    Confusion matrix:
                        broad-leaved forest built-up area coniferous forest fields meadows natural grasslands rocks scrub water class.error
    broad-leaved forest                 225             0                 0      0       0                  0     0     0     0 0.000000000
    built-up area                         0           222                 0      0       0                  0     2     0     1 0.013333333
    coniferous forest                     0             0               225      0       0                  0     0     0     0 0.000000000
    fields                                0             0                 0    224       1                  0     0     0     0 0.004444444
    meadows                               0             0                 0      0     225                  0     0     0     0 0.000000000
    natural grasslands                    0             0                 0      0       0                225     0     0     0 0.000000000
    rocks                                 0             5                 0      0       0                  0   220     0     0 0.022222222
    scrub                                 0             0                 0      0       0                  0     0   225     0 0.000000000
    water                                 0             0                 0      0       0                  0     0     0   225 0.000000000

The confusion matrix What we really want to do is to measure the model performance against the data it hasn’t been trained on. To do that we will use `valData` prepared earlier. We will then compare the predicted classes with actual one in the test layer.

``` r
predicted_rf <- predict(model_rf, valData[ , 1:length(image@data@names)])


confusion_matrix_predicted_rf <- confusionMatrix(predicted_rf, as.factor(valData$class), mode = "everything")

confusion_matrix_predicted_rf
```

    > confusion_matrix_predicted_rf
    Confusion Matrix and Statistics

                         Reference
    Prediction            broad-leaved forest built-up area coniferous forest fields meadows natural grasslands rocks scrub water
      broad-leaved forest                 217             0                 9      0       0                  0     0     0     0
      built-up area                         0           200                 0      0       0                  0    25     2     0
      coniferous forest                     3             0               208      0       0                  0     0     9     0
      fields                                0             6                 0    192      49                  0     0     0     0
      meadows                               0             2                 0     33     167                 19     0     2     0
      natural grasslands                    0             0                 0      0       9                206     0     0     0
      rocks                                 0            10                 0      0       0                  0   200     7     0
      scrub                                 5             1                 8      0       0                  0     0   205     0
      water                                 0             6                 0      0       0                  0     0     0   225

    Overall Statistics
                                              
                   Accuracy : 0.8988          
                     95% CI : (0.8848, 0.9116)
        No Information Rate : 0.1111          
        P-Value [Acc > NIR] : < 2.2e-16       
                                              
                      Kappa : 0.8861          
                                              
     Mcnemar's Test P-Value : NA              

    Statistics by Class:

                         Class: broad-leaved forest Class: built-up area Class: coniferous forest Class: fields Class: meadows
    Sensitivity                              0.9644              0.88889                   0.9244       0.85333        0.74222
    Specificity                              0.9950              0.98500                   0.9933       0.96944        0.96889
    Pos Pred Value                           0.9602              0.88106                   0.9455       0.77733        0.74888
    Neg Pred Value                           0.9956              0.98610                   0.9906       0.98144        0.96781
    Precision                                0.9602              0.88106                   0.9455       0.77733        0.74888
    Recall                                   0.9644              0.88889                   0.9244       0.85333        0.74222
    F1                                       0.9623              0.88496                   0.9348       0.81356        0.74554
    Prevalence                               0.1111              0.11111                   0.1111       0.11111        0.11111
    Detection Rate                           0.1072              0.09877                   0.1027       0.09481        0.08247
    Detection Prevalence                     0.1116              0.11210                   0.1086       0.12198        0.11012
    Balanced Accuracy                        0.9797              0.93694                   0.9589       0.91139        0.85556
                         Class: natural grasslands Class: rocks Class: scrub Class: water
    Sensitivity                             0.9156      0.88889       0.9111       1.0000
    Specificity                             0.9950      0.99056       0.9922       0.9967
    Pos Pred Value                          0.9581      0.92166       0.9361       0.9740
    Neg Pred Value                          0.9895      0.98617       0.9889       1.0000
    Precision                               0.9581      0.92166       0.9361       0.9740
    Recall                                  0.9156      0.88889       0.9111       1.0000
    F1                                      0.9364      0.90498       0.9234       0.9868
    Prevalence                              0.1111      0.11111       0.1111       0.1111
    Detection Rate                          0.1017      0.09877       0.1012       0.1111
    Detection Prevalence                    0.1062      0.10716       0.1081       0.1141
    Balanced Accuracy                       0.9553      0.93972       0.9517       0.9983

<b><u>TASK</u></b>

Identify classes with highest and lowest accuracy metrics.

### Variable importance

Based on the model we can also identify best performing predictors (bands). We saved the `importance` values inside the model stored in `model_rf` variable. To display them as plot we can use `varImpPlot` function from `randomForest` package.

``` r
varImpPlot(model_rf, type = 1)
```

<center>

<img src="media_exercise/var_imp_plot.png" title="variable importance" alt="variable importance" width="700"/>

<i>Variable importance plot.</i>
</center>

<b><u>TASK</u></b>

Identify bands with the most significant impact on the classification.

### Image prediction

Finally, we can apply the acquired model to the image data we have to produce classification image. `predict` function from the `raster` package need.

``` r
raster::predict(image, model_rf, filename = "predicted_image_all_bands.tif", datatype = "INT1U", progress = "text")
```

<b><u>TASK</u></b>

Display the resulting image in QGIS using the attached **symbology.clr** file to apply class names and colors.

<center>

<img src="media_exercise/predicted_image.PNG" title="Predicted image" alt="Predicted image" width="1000"/>

<i>Predicted image (all variables).</i>
</center>

## Classification scenario 2 (only spectral bands) and scenario 3 (only NDVI bands)

The goal of the first scenario was to guide you through the simple classification process from start to finish. Now that you acknowledged yourself with the method you will go through scenarios 2 and 3 by your own.

The workflow stays the same, although you need to truncate the reference data to include only values from specific bands.

<details>
<summary>
Reference for classification scenario 2
</summary>

``` r
reference_scenario2 <- pixel_reference[, c(1:10, 12:21, 23:32, 34:43, 45:54, 56:65, 67:68)]
```

</details>
<details>
<summary>
Reference for classification scenario 3
</summary>

``` r
reference_scenario3 <- pixel_reference[, c(11, 22, 33, 44, 55, 66, 67:68)]
```

</details>

<b><u>TASK</u></b>

- Divide reference datasets into training and validation.
- Tune `mtry` parameter.
- Create and save Random Forest classification model.
- Apply the model to test data and image.
- Compare the accuracy results and visual images.

## Results comparison & discussion

Points to test by the students: extract single term and perform classification, extract only best performing bands based on variable importance and repeat classification, test different mtry values etc.
