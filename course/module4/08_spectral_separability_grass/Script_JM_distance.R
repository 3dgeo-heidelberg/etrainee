#June:data=read.delim("Rin_grasses_2020_06.txt");
#July: data=read.delim("Rin_grasses_2020_07.txt");
data=read.delim("Rin_grasses_2020_08.txt");

fix(data)

d=dim(data)
d

attach(data)

# JM distance for all bands together
JMdist2(classname, data[,2:55])

# JM distance for separate bands (August example, rename the output text file for other months)
results <- matrix() # definition of the empty matrix 
JM_band1 <- JMdist2(classname, data[,2]) # calculation of JM distance for the first band
JM_band1 # JM distance for the first band, you can copy the combination of classes here, it remains the same also in the loop
results <- JM_band1$jmdist # save the JM distance for first band to the empty matrix (it gives the structure to the matrix)

for (I in 3:55) # the loop for bands 2 - 54
{
	JM_band <- JMdist2(classname, data[,I])	# calculate JM distance for band I 
	results <- rbind(results, JM_band$jmdist); # save result for the I band as a new row to the matrix "results"
}

write.table(results, "JM_distance2_bands_August.txt") # save the results for all the bands to the text file
