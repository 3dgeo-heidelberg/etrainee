Case study: Forest disturbance detection (Tatras)
================

## Case study: Forest disturbance detection (Tatra Mountains)

The aim of this case study is similar as in Theme 5 exercise but this time we will use the **Threshold and trend-based vegetation change monitoring algorithm (TVCMA)** instead of the LandTrendr (see the first three paragraphs of [Theme 5 exercise](../05_vegetation_monitoring/05_vegetation_monitoring_exercise.md). TVCMA was developed in R language for that reason we will use scripts in R. We will use the same dataset, only one difference is related to raster file structure due to different requirements for input data preparation for both algorithms. We will use part of the capabilities of TVCMA which are related to detection of time and location of forest disturbance events based on thresholding and logical rules.

Before you continue, get familiar with the use case (if you did it before in Theme 5 you can skip this step): **[Use case: Vegetation disturbance detection in Polish-Slovak Tatra Mountains](../../data_usecases/usecase_forest_tatras.md)**.

… and read the paper accompanying the use case: Ochtyra, A., Marcinkowska-Ochtyra, A., & Raczko, E. (2020). Threshold and trend-based vegetation change monitoring algorithm based on the inter-annual multi-temporal normalized difference moisture index series: A case study of the Tatra Mountains. Remote Sensing of Environment, 249, 112026. <https://doi.org/10.1016/j.rse.2020.112026>

Our work will be divided on three main parts:

1.  Extraction of values tested variables time series using reference data points.

2.  Testing of a variety of variables and threshold values with accuracy assessment.

3.  Calculation of resulting rasters presenting detected disturbance events.

## Getting started

### Environment preparation: loading required libraries and data

To start with, we want to load necessary libraries and data and set up some initial variables, which we will use further down the line. Firstly, load required libraries into the environment: rgdal, raster, dplyr, sf, readxl, and writexl. Functions included in these packages will be used further in this case study.

``` r
library(rgdal) # spatial data processing
library(raster) # raster processing
library(dplyr) #    
library(readxl) # 
library(writexl) # 
```

Now we can start with loading up the required data. We will start with the raster data which are a time series of vegetation indices and products Tasseled Cap transformation calculated on Landsat cloud-free composites from 1984 to 2022 prepared in [Theme 3 exercise, pipeline 2](../03_image_processing/03_image_processing_exercise.md#processing-pipeline-2).

``` r
ndvi <- brick("F:/ETR/rmd/dane_cs3/_final_v1/img_data/NDVI_revised.tif")
nbr <- brick("F:/ETR/rmd/dane_cs3/_final_v1/img_data/NBR_revised.tif")
nbr2 <- brick("F:/ETR/rmd/dane_cs3/_final_v1/img_data/NBR2_revised.tif")
ndmi <- brick("F:/ETR/rmd/dane_cw5/data/doy/NDMI_filled.tif")
ndwi <- brick("F:/ETR/rmd/dane_cs3/_final_v1/img_data/NDWI_revised.tif")
tcb <- brick("F:/ETR/rmd/dane_cs3/_final_v1/img_data/TCB_revised.tif")
tcg <- brick("F:/ETR/rmd/dane_cs3/_final_v1/img_data/TCG_revised.tif")
tcw <- brick("F:/ETR/rmd/dane_cs3/_final_v1/img_data/TCW_revised.tif")
```

Note: you can prepare your own time series of variables which you would like to test

Now we will upload vector layer data which contains 100 reference points. It will be used for extraction values from rasters loaded in the previous step.

``` r
pkt <- st_read("F:/ETR/rmd/dane_cw5/punkty_100/punkty_100.shp")
```

Next we go to values extraction from all prepared time series.

``` r
ndvi_vals <- extract(ndvi, pkt, df = TRUE) %>%
  select(2:40)

colnames(ndvi_vals) <- c("NDVI_1984", "NDVI_1985", "NDVI_1986", "NDVI_1987", "NDVI_1988", "NDVI_1989", "NDVI_1990",
                         "NDVI_1991",
                         "NDVI_1992", "NDVI_1993", "NDVI_1994", "NDVI_1995", "NDVI_1996", "NDVI_1997", "NDVI_1998", "NDVI_1999",
                         "NDVI_2000", "NDVI_2001", "NDVI_2002", "NDVI_2003", "NDVI_2004", "NDVI_2005", "NDVI_2006", "NDVI_2007",
                         "NDVI_2008", "NDVI_2009", "NDVI_2010", "NDVI_2011", "NDVI_2012", "NDVI_2013", "NDVI_2014",
                         "NDVI_2015", "NDVI_2016", "NDVI_2017", "NDVI_2018",  "NDVI_2019",  "NDVI_2020", "NDVI_2021", "NDVI_2022")


ndmi_vals <- extract(ndmi, pkt, df = TRUE) %>%
  select(2:40)
colnames(ndmi_vals) <- c("NDMI_1984", "NDMI_1985", "NDMI_1986", "NDMI_1987", "NDMI_1988", "NDMI_1989", "NDMI_1990",
                         "NDMI_1991",
                         "NDMI_1992", "NDMI_1993", "NDMI_1994", "NDMI_1995", "NDMI_1996", "NDMI_1997", "NDMI_1998", "NDMI_1999", 
                         "NDMI_2000", "NDMI_2001", "NDMI_2002", "NDMI_2003", "NDMI_2004", "NDMI_2005", "NDMI_2006", "NDMI_2007", 
                         "NDMI_2008", "NDMI_2009", "NDMI_2010", "NDMI_2011", "NDMI_2012", "NDMI_2013", "NDMI_2014", 
                         "NDMI_2015", "NDMI_2016", "NDMI_2017", "NDMI_2018",  "NDMI_2019",  "NDMI_2020", "NDMI_2021", "NDMI_2022")

ndwi_vals <- extract(ndwi, pkt, df = TRUE) %>%
  select(2:40)
colnames(ndwi_vals) <- c("NDWI_1984", "NDWI_1985", "NDWI_1986", "NDWI_1987", "NDWI_1988", "NDWI_1989", "NDWI_1990",
                         "NDWI_1991",
                         "NDWI_1992", "NDWI_1993", "NDWI_1994", "NDWI_1995", "NDWI_1996", "NDWI_1997", "NDWI_1998", "NDWI_1999", 
                         "NDWI_2000", "NDWI_2001", "NDWI_2002", "NDWI_2003", "NDWI_2004", "NDWI_2005", "NDWI_2006", "NDWI_2007", 
                         "NDWI_2008", "NDWI_2009", "NDWI_2010", "NDWI_2011", "NDWI_2012", "NDWI_2013", "NDWI_2014", 
                         "NDWI_2015", "NDWI_2016", "NDWI_2017", "NDWI_2018",  "NDWI_2019",  "NDWI_2020", "NDWI_2021", "NDWI_2022")


nbr_vals <- extract(nbr, pkt, df = TRUE) %>%
  select(2:40)

colnames(nbr_vals) <- c("NBR_1984", "NBR_1985", "NBR_1986", "NBR_1987", "NBR_1988", "NBR_1989", "NBR_1990",
                         "NBR_1991",
                         "NBR_1992", "NBR_1993", "NBR_1994", "NBR_1995", "NBR_1996", "NBR_1997", "NBR_1998", "NBR_1999",
                         "NBR_2000", "NBR_2001", "NBR_2002", "NBR_2003", "NBR_2004", "NBR_2005", "NBR_2006", "NBR_2007",
                         "NBR_2008", "NBR_2009", "NBR_2010", "NBR_2011", "NBR_2012", "NBR_2013", "NBR_2014",
                         "NBR_2015", "NBR_2016", "NBR_2017", "NBR_2018",  "NBR_2019",  "NBR_2020", "NBR_2021", "NBR_2022")


nbr2_vals <- extract(nbr2, pkt, df = TRUE) %>%
  select(2:40)

colnames(nbr2_vals) <- c("NBR2_1984", "NBR2_1985", "NBR2_1986", "NBR2_1987", "NBR2_1988", "NBR2_1989", "NBR2_1990",
                        "NBR2_1991",
                        "NBR2_1992", "NBR2_1993", "NBR2_1994", "NBR2_1995", "NBR2_1996", "NBR2_1997", "NBR2_1998", "NBR2_1999",
                        "NBR2_2000", "NBR2_2001", "NBR2_2002", "NBR2_2003", "NBR2_2004", "NBR2_2005", "NBR2_2006", "NBR2_2007",
                        "NBR2_2008", "NBR2_2009", "NBR2_2010", "NBR2_2011", "NBR2_2012", "NBR2_2013", "NBR2_2014",
                        "NBR2_2015", "NBR2_2016", "NBR2_2017", "NBR2_2018",  "NBR2_2019",  "NBR2_2020", "NBR2_2021", "NBR2_2022")


tcg_vals <- extract(tcg, pkt, df = TRUE) %>%
  select(2:40)

colnames(tcg_vals) <- c("TCG_1984", "TCG_1985", "TCG_1986", "TCG_1987", "TCG_1988", "TCG_1989", "TCG_1990",
                        "TCG_1991",
                        "TCG_1992", "TCG_1993", "TCG_1994", "TCG_1995", "TCG_1996", "TCG_1997", "TCG_1998", "TCG_1999", 
                        "TCG_2000", "TCG_2001", "TCG_2002", "TCG_2003", "TCG_2004", "TCG_2005", "TCG_2006", "TCG_2007", 
                        "TCG_2008", "TCG_2009", "TCG_2010", "TCG_2011", "TCG_2012", "TCG_2013", "TCG_2014", 
                        "TCG_2015", "TCG_2016", "TCG_2017", "TCG_2018",  "TCG_2019",  "TCG_2020", "TCG_2021", "TCG_2022")

tcb_vals <- extract(tcb, pkt, df = TRUE) %>%
  select(2:40)

colnames(tcb_vals) <- c("TCB_1984", "TCB_1985", "TCB_1986", "TCB_1987", "TCB_1988", "TCB_1989", "TCB_1990",
                        "TCB_1991",
                        "TCB_1992", "TCB_1993", "TCB_1994", "TCB_1995", "TCB_1996", "TCB_1997", "TCB_1998", "TCB_1999", 
                        "TCB_2000", "TCB_2001", "TCB_2002", "TCB_2003", "TCB_2004", "TCB_2005", "TCB_2006", "TCB_2007", 
                        "TCB_2008", "TCB_2009", "TCB_2010", "TCB_2011", "TCB_2012", "TCB_2013", "TCB_2014", 
                        "TCB_2015", "TCB_2016", "TCB_2017", "TCB_2018",  "TCB_2019",  "TCB_2020", "TCB_2021", "TCB_2022")


tcw_vals <- extract(tcw, pkt, df = TRUE) %>%
  select(2:40)

colnames(tcw_vals) <- c("TCW_1984", "TCW_1985", "TCW_1986", "TCW_1987", "TCW_1988", "TCW_1989", "TCW_1990",
                        "TCW_1991",
                        "TCW_1992", "TCW_1993", "TCW_1994", "TCW_1995", "TCW_1996", "TCW_1997", "TCW_1998", "TCW_1999", 
                        "TCW_2000", "TCW_2001", "TCW_2002", "TCW_2003", "TCW_2004", "TCW_2005", "TCW_2006", "TCW_2007", 
                        "TCW_2008", "TCW_2009", "TCW_2010", "TCW_2011", "TCW_2012", "TCW_2013", "TCW_2014", 
                        "TCW_2015", "TCW_2016", "TCW_2017", "TCW_2018",  "TCW_2019",  "TCW_2020", "TCW_2021", "TCW_2022")
```

After values extraction we will bind all columns with data to one table to have one dataset for testing.

``` r
pkt2 <- bind_cols(pkt, ndvi_vals, nbr_vals, nbr2_vals, ndmi_vals, ndwi_vals, tcb_vals, tcg_vals, tcw_vals)
```

Last step of this part will be saving a vector layer with extracted values.

``` r
st_write(pkt2, "F:/ETR/rmd/dane_cs3/_final_v1/points_100_values.shp")
```

Now we have a vector file of reference data with extracted values from our variables, such prepared data we will use in the second main step.

## Testing variables utility, model optimization and accuracy assessment

In this step we will focus on searching for the best variable and threshold value for forest disturbance detection. In the begining we will upload a previously prepared vector layer.

``` r
input_data <- st_read("F:/ETR/rmd/dane_cs3/_final_v1/vect_data/CS3_points_with_raster_values.shp")
```

Now we will divide the table with the variables values to receive new tables containing values of each variable separately, this allows us to test the performance of the algorithm on each dataset individually.

``` r
ndvi_data <- input_data %>%
  st_drop_geometry() %>%
  select(2:40)


nbr_data <- input_data %>%
  st_drop_geometry() %>%
  select(41:79)


nbr2_data <- input_data %>%
  st_drop_geometry() %>%
  select(80:118)


ndmi_data <- input_data %>%
  st_drop_geometry() %>%
  select(119:157)

ndwi_data <- input_data %>%
  st_drop_geometry() %>%
  select(158:196)

tcb_data <- input_data %>%
  st_drop_geometry() %>%
  select(197:235)

tcg_data <- input_data %>%
  st_drop_geometry() %>%
  select(236:274)

tcw_data <- input_data %>%
  st_drop_geometry() %>%
  select(275:313)
```

For accuracy assessment we need to upload the table containing information about years of disturbances occurrence. In rows are recorded subsequent reference points, in columns are recorded subsequent years, if disturbance was not observed „0” value was assigned in the proper cell, if disturbance was observed „1” value was assigned in proper cell.

``` r
validation_data <- read_excel("F:/ETR/rmd/dane_cs3/_final_v1/warstwa_walidacyjna.xlsx")
```

Here we fix which variable we will use in the testing phase. Each variable needs to be set separately. In this example we have chosen NDVI.

``` r
Validation_data <- validation_data  %>%
  .[, 2:39]
```

Now we will use a function which is an implementation of TVCMA in R and it will be proceeded on a time series of extracted variable values for each reference point separately. Thus we can optimize threshold value to receive the best results without need to use the whole raster series. This allows us on faster processing. After we select best variable and threshold value we will use proper raster time series to generate disturbances maps in the third main step of this case study. The function contains logical rules that have to be met to mark a given pixel in a given year as a detected disturbance. Note that the basic set of rules takes into account four dates (observations) from time series: actually analysed observation, the one following and two preceding. In case of the second and the last observations it obviously can not be done for that reason sets of rules for them are modified properly.

``` r
apply_tvcma_conditions_points <- function(ind, threshold) {
  
  res <- matrix(data = FALSE, nrow = nrow(ind), ncol = ncol(ind))
  
  for (i in 1:nrow(ind)) {
    for (j in 3:(ncol(ind) - 1)) {
      if (threshold >= 0) {
        cond_1 <- (ind[i, j] - ind[i, j - 1]) > threshold
        cond_2 <- (ind[i, j + 1] - ind[i, j - 1]) > threshold
        cond_3 <- (ind[i, j] - ind[i, j - 2]) > threshold
      } else {
        cond_1 <- (ind[i, j] - ind[i, j - 1]) < threshold
        cond_2 <- (ind[i, j + 1] - ind[i, j - 1]) < threshold
        cond_3 <- (ind[i, j] - ind[i, j - 2]) < threshold
      }
     res[i, j] <- cond_1 & cond_2 & cond_3
    }
    # For the second observation, it should meet cond_1 and cond_2
    if (threshold >= 0) {
      cond_1_second <- (ind[i, 2] - ind[i, 1]) > threshold
      cond_2_second <- (ind[i, 3] - ind[i, 1]) > threshold
    } else {
      cond_1_second <- (ind[i, 2] - ind[i, 1]) < threshold
      cond_2_second <- (ind[i, 3] - ind[i, 1]) < threshold
    }
    res[i, 2] <- cond_1_second & cond_2_second
    
    # For the last observation, it should meet cond_1 and cond_3
    if (threshold >= 0) {
      cond_1_last <- (ind[i, ncol(ind)] - ind[i, ncol(ind) - 1]) > threshold
      cond_3_last <- (ind[i, ncol(ind)] - ind[i, ncol(ind) - 2]) > threshold
    } else {
      cond_1_last <- (ind[i, ncol(ind)] - ind[i, ncol(ind) - 1]) < threshold
      cond_3_last <- (ind[i, ncol(ind)] - ind[i, ncol(ind) - 2]) < threshold
    }
    res[i, ncol(ind)] <- cond_1_last & cond_3_last
  }
  
  # Remove the first column from resulting matrix
  res <- res[,2:ncol(res)]
  
  return(res)
}
```

After we add the function we go to automatization of testing threshold values. Here we can specify in which values range it will be tested and with which step.

``` r
thresholds <- seq(-0.005, -0.02, by = -0.001)
```

To choose the best variable and threshold value we will create a table with accuracy assessment results where each row will be containing results for one threshold value. To make selection easy, in the table each record will be named which include information about used threshold value.

``` r
names_list <- paste0("Threshold_", gsub("\\.", "_", abs(thresholds))) # replace "." with "_"


# Check threshold 

results <- setNames(lapply(thresholds, apply_tvcma_conditions_points, ind = tcg_data), names_list)
```

To calculate accuracy metrics in the beginning we need to count numbers of True Positives, False Positives, True Negatives and False Negatives. To do it we will compare the reference table with the resulting table for each tested threshold value. As it was mentioned before in the reference table, the date of disturbance occurrence is marked as “1” and the rest of dates are marked as “0”. The algorithm produces results in the same manner so we can check according to the cell values of both tables, e.g. in reference data for a given point in a given was marked “1” and when the resulting table also shows “1” it means that is True Positive.

``` r
# Function to calculate confusion matrix stats
calculate_confusion_matrix_stats <- function(matrix, validation_matrix, set_name) {
  # Calculate TP, FP, TN, FN
  TP <- sum(matrix == 1 & validation_matrix == 1)
  FP <- sum(matrix == 1 & validation_matrix == 0)
  TN <- sum(matrix == 0 & validation_matrix == 0)
  FN <- sum(matrix == 0 & validation_matrix == 1)
```

Now we can calculate several accuracy metrics to select the best model.

``` r
calculate_confusion_matrix_stats <- function(matrix, validation_matrix, set_name) {
  # Calculate TP, FP, TN, FN
  TP <- sum(matrix == 1 & validation_matrix == 1)
  FP <- sum(matrix == 1 & validation_matrix == 0)
  TN <- sum(matrix == 0 & validation_matrix == 0)
  FN <- sum(matrix == 0 & validation_matrix == 1)
  
  # Calculate the metrics
  Accuracy <- (TP + TN) / (TP + FP + FN + TN)
  Precision <- TP / (TP + FP)
  Sensitivity <- TP / (TP + FN)
  Specificity <- TN / (TN + FP)
  F1_Score <- 2 * (Sensitivity * Precision) / (Sensitivity  + Precision)
Now we create a data frame to save the confusion matrices.

# Create a data frame with the confusion matrix stats
  stats <- data.frame(Set = set_name, TP, FP, TN, FN, Accuracy, Precision, Sensitivity, Specificity, F1_Score)
  
  return(stats)
}
```

We would like to calculate accuracy metrics for each threshold value which we are testing…

``` r
# Calculate confusion matrix for each threshold tested
stats_list <- lapply(seq_along(results), function(i) calculate_confusion_matrix_stats(results[[i]], validation_data, names(results)[i]))
```

… bind the results in one table…

``` r
# one table with confusion results
stats_df <- do.call(rbind, stats_list)
```

… and save them as an .xlsx file.

``` r
write_xlsx(stats_df, "F:/ETR/rmd/dane_cs3/_final_v1/res/tcg_-0005_-002_-0001_confusion_matrix_stats.xlsx")
```

When you finally test all variables and selected thresholds, compare results and choose the best one based on accuracy metrics. The third and the last step will be disturbance maps producing. In the beginning we load a time series of previously selected variables…

``` r
multiband_raster <- brick("F:/ETR/rmd/dane_cw5/data/doy/NDMI_filled.tif")
```

… and we will set a chosen threshold.

``` r
threshold <- -0.05
```

We need to create an array to save the results.

``` r
result_array <- array(0, dim = c(nrow(multiband_raster), ncol(multiband_raster), nlayers(multiband_raster) - 1))
```

Now we will use algorithm conditions to produce maps.

``` r
for (i in 1:nrow(multiband_raster)) {
    print(i)
  row_values <- getValuesBlock(multiband_raster, row = i, nrows = 1, col = 1, ncols = ncol(multiband_raster))

  results <- rep(NA, ncol(multiband_raster) * (nlayers(multiband_raster) - 1))
  
  for (k in 1:nrow(row_values)) {
    
    values <- row_values[k, ]
    val_len <- length(values)
    
    if (threshold >= 0) {
      
      cond_1 <- (values[3:((val_len) - 1)] - values[2:(val_len - 2)]) > threshold
      cond_2 <- (values[4:(val_len)] - values[2:(val_len - 2)]) > threshold
      cond_3 <- (values[3:((val_len) - 1)] - values[1:(val_len - 3)]) > threshold
      
      r1 <- cond_1 & cond_2 & cond_3
      r2 <- (values[2] - values[1]) > threshold & (values[3] - values[1]) > threshold
      r3 <- (values[val_len] - values[val_len - 1]) > threshold & (values[val_len] - values[val_len - 2]) > threshold
      
    } else {
      
      cond_1 <- (values[3:((val_len) - 1)] - values[2:(val_len - 2)]) < threshold
      cond_2 <- (values[4:(val_len)] - values[2:(val_len - 2)]) < threshold
      cond_3 <- (values[3:((val_len) - 1)] - values[1:(val_len - 3)]) < threshold
      
      r1 <- cond_1 & cond_2 & cond_3
      r2 <- (values[2] - values[1]) < threshold & (values[3] - values[1]) < threshold
      r3 <- (values[val_len] - values[val_len - 1]) < threshold & (values[val_len] - values[val_len - 2]) < threshold
    }
    
    result <- c(r2, r1, r3)
    results[(((k - 1) * (val_len - 1)) + 1):(k * (val_len - 1))] <- result
    
  }
```

…

``` r
  n_layers_minus_one <- nlayers(multiband_raster) - 1
  
  for (j in 1:ncol(multiband_raster)) {
    
    index_start <- (j - 1) * n_layers_minus_one + 1
    index_end <- j * n_layers_minus_one
    result_array[i, j, ] <- results[index_start:index_end]
  }
}

result_brick <- brick(result_array,
                      xmn = xmin(multiband_raster),
                      xmx = xmax(multiband_raster),
                      ymn = ymin(multiband_raster),
                      ymx = ymax(multiband_raster),
                      crs = crs(multiband_raster)
)
```

In the end we will save the resulting rasters as a multiband raster file where each band presents detected disturbances in a certain year from the analysed time series, obviously without the first one for which we cannot detect disturbance using this algorithm.

``` r
writeRaster(result_brick, "ndmi_-005_full_fix.tif")
```

## Discussion

## Points to discuss:

- 
- 
- 

## References

### Other case studies

- [Monitoring tundra grasslands (Karkonosze)](../06_cs_tundra_grasslands/06_cs_tundra_grasslands.md)
- [Effects of pollution (Ore Mountains)](07_cs_forest_changes/07_cs_forest_changes.md)

### Module themes

- [Principles of multispectral imaging](../01_multispectral_principles/01_multispectral_principles.md)
- [Temporal information in satellite data](../02_temporal_information/02_temporal_information.md)
- [Image processing workflow](../03_image_processing/03_image_processing.md)
- [Multitemporal classification of vegetation types](../04_multitemporal_classification/04_multitemporal_classification.md)
- [Vegetation monitoring and disturbance detection](../05_vegetation_monitoring/05_vegetation_monitoring.md)
