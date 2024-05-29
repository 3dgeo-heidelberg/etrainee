# E-TRAINEE Module 4: Airborne Imaging Spectroscopy Time Series Analysis
# Case study: monitoring tundra grasslands in the Krkonoše Mountains

# =============================================================================
# Import libraries
# This loads required packages (and installs them if necessary)
l_packages <- c("raster", "rgdal", "randomForest", "glcm", "spacetime")
for (package in l_packages){
  if(! package %in% installed.packages()){
    install.packages(package, dependencies = TRUE)
  }
  library(package, character.only = T)
}

# Set working directory - insert path to your data
setwd("c:/path/to/data")
getwd()

# =============================================================================
# 1.
# Monotemporal dataset - uncomment this part to perform classification on one of the monotemporal datasets
# =============================================================================
# Load input hyperspectral (HS) image
img <- brick("BL_202006.tif")
# Assign band names to image
names(img) <-  paste0("B", c(1:54))

# =============================================================================
# 2.
# Multitemporal composite - uncomment this part to composite the two datasets
# =============================================================================
#img_1 <- brick("BL_202006.tif")
#img_2 <- brick("BL_202008.tif")
#img   <- stack(img_1, img_2)
# Assign band names to image
#names(img) <-  paste0("B", c(1:108))




# =============================================================================
# Load training data
# =============================================================================
# Load vector training data
training <- readOGR(dsn=getwd(), layer="train_polygons") # dsn name of folder containing shp, with the name in layer
View(training)

# Vizualize of image and training data for control
plot(img$B3)
plot(training, bg="transparent", add=TRUE)

# =============================================================================
# Feature extraction
# =============================================================================
# Calculate GLCM textures from each spectral band
# TAKES LONG TIME!!!
out <- list()
for(band in 1:dim(img)[3]) {
  out[band] <- glcm::glcm(img[[band]], window = c(3, 3), na_opt = 'center', 
                       statistics = c("mean", "variance", "homogeneity", "contrast",
                                      "dissimilarity", "entropy", "second_moment"))
  print(paste0('Finished computing textures for band #', band, '/', dim(img)[3]))
}
textures <- stack(out)

# Stack image and textures
predictors <- stack(img, textures)

# Preparation of training data
# Extract raster values from training polygons
df_features <- extract(predictors, training, df=TRUE) # TAKES LONG TIME!!!

# Remove rows with nodata values
training <- na.omit(df_features)
# Rename column ID to Classvalue
names(training)[names(training) == 'ID'] <- 'Classvalue'

# See number of features for each class
table(training$Classvalue)

# =============================================================================
# Train + Apply a RF model
# =============================================================================
# TAKES LONG TIME!!
model <- randomForest(as.factor(Classvalue) ~.,data=training,
                      ntree=100, importance=TRUE, do.trace=50) ### original model had ntree=1000

# Classify image using trained model
predicted <- predict(predictors, model)

# Vizualize classification
plot(predicted, main = 'Classification Random Forest')

# Print information about the trained model
model

# =============================================================================
# Export results
# =============================================================================
# Export feature importance table
feature_importance <- model$importance
write.table(feature_importance, "BL_202006_RF_feature_importance.txt")

# Save classification as a raster
writeRaster(predicted, filename="BL_202006_RF_classified.tif",overwrite=TRUE)
Sys.time()
