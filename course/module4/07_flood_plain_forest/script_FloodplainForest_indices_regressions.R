data=read.delim("FloodplainForest_2019_training.txt") # upload data
fix(data)	# view data
attach(data)	

# Chlorophyll content indices
# Main et al. 2011

MCARI=((X700-X670)-0.2*(X700-X550))*(X700/X670) 	# (Main et al. 2011; Daughtry et al. 2000)
MCARI2=((X750-X705)-0.2*(X750-X550))*(X750/X705)    # (Main et al. 2011; Wu et al. 2008)
TCARI=3*((X700-X670)-0.2*(X700-X550)*(X700/X670)) 	# (Main et al. 2011; Haboudane et al. 2002)
OSAVI=(1+0.16)*(X800-X670)/(X800+X670+0.16)  		# (Main et al. 2011; Rondeaux et al 1996)
OSAVI2=(1+0.16)*(X750-X705)/(X750+X705+0.16) 		#  (Main et al. 2011; Wu et al. 2008)
TCARIOSAVI=TCARI/OSAVI  							# (Main et al. 2011; Haboudane et al. 2002)
MCARIOSAVI=MCARI/OSAVI   							# (Main et al. 2011; Daughtry et al. 2000)
MCARI2OSAVI2=MCARI2/OSAVI2                          # (Main et al. 2011; Wu et al. 2008)
TVI=0.5*(120*(X750-X550)-200*(X670-X550))    		# (Main et al. 2011; Broge and Leblanc 2000)
MTCI=(X754-X709)/(X709-X681)       		  # (Main et al. 2011; Dash and Curran 2004)
mND705=(X750-X705)/(X750+X705-2*X445)     # (Main et al. 2011; Sims and Gamon 2002)
Gitelson2=(X750-X800/X695-X740)-1         # (Main et al. 2011; Gitelson et al. 2003)
Maccioni=(X780-X710)/(X780-X680)          # (Main et al. 2011; Maccioni et al. 2001)
Vogelmann=X740/X720                       # (Main et al. 2011; Vogelmann et al. 1993)
Vogelmann2=(X734-X747)/(X715+X726)        # (Main et al. 2011; Vogelmann et al. 1993)
Datt=(X850-X710)/(X850-X680)              # (Main et al. 2011; Datt 1999)
Datt2=X850/X710                           # (Main et al. 2011; Datt 1999)
SR1=X750/X710                             # (Main et al. 2011; Zarco-Tejada and Miller 1999); oznaceno jako CIrededge v Hernandez-Clemente
SR2=X440/X690 				  			  # (Main et al. 2011;Lichtenthaler et al. 1996)
DD=(X749-X720)-(X701-X672)                # (Main et al. 2011; le Maire et al. 2004); (Double Difference Index)
Carter=X695/X420                          # (Main et al. 2011; Carter 1994)
Carter2=X710/X760                         # (Main et al. 2011; Carter 1994)
REP_LI=700+40*((X670+X780/2)/(X740-X700)) # (Main et al. 2011; Guyot and Baret 1988)

# Misurec et al. 2016

REP=700+40*((((X670+X780)/2)-X700)/(X740-X700)) 	# (Misurec 2016; Curran et al 1995)
RDVI=(X800-X670)/sqrt(X800+X670)  					# (Misurec 2016; Roujean and Breon 1995)
MSR=((800-670)-1)/sqrt((X800/X670)+1) 				# (Misurec 2016; Chen 1996 )
MSAVI=0.5*((2*X800+1-sqrt((X800+1)^(2))-8*(X800-X670))) 	# (Misurec 2016; Qi et al. 1994)
N705=(X705-X675)/(X750-X670)						# (Misurec 2016; Campbell et al. 2004)
N715=(X715-X675)/(X750-X670)						# (Misurec 2016; Campbell et al. 2004)
N725=(X725-X675)/(X750-X670)                     	# (Misurec 2016; Campbell et al. 2004)

# adding indices to original table

dataVI=(cbind(data,MCARI,MCARI2,TCARI,OSAVI,OSAVI2,TCARIOSAVI,MCARIOSAVI,MCARI2OSAVI2,TVI,MTCI,mND705,Gitelson2,Maccioni,Vogelmann,Vogelmann2,Datt,Datt2,SR1,SR2,DD,Carter,Carter2,REP_LI,REP,RDVI,MSR,MSAVI,
N705,N715,N725))

write.table(dataVI,"FloodplainForest_2019_training_indices.txt") # saving data and indices to the text file

fix(dataVI)	# view data + indices

# explore what are the dimensions of the original table and table with indices; next for loop will be computed only for indices, i. e. from the number of columns od original data plus one till the end
dim(data)
dim(dataVI)

# creating of empty vectors
results_p <- vector()
results_R <- vector()
results_i <- vector()
results_koef <- vector()

# computing linear regression model between indices and laboratory chlorophyll content in for loop and saving the p-values, coeficient of determination and equation coefficients to the text files
for (I in 2159:2188) # change the values of I based on the results of dim function
{
model<-lm(dataVI$Total_chloro_ug_cm2~dataVI[,I]);
sum=summary(model)
out<-capture.output(sum);
results_p <- append(results_p,grep ("p-value", out, value = TRUE) );
results_R <- append(results_R,grep ("Multiple R-squared", out, value = TRUE) );
results_i <- append(results_i,grep ("(Intercept)", out, value = TRUE) );
results_koef <- append(results_koef,grep ("dataVI", out, value = TRUE) );
}
 
write(results_p, "2019_Tot_chl_results_p.txt")
write(results_R, "2019_Tot_chl_results_R.txt")
write(results_i, "2019_Tot_chl_results_i.txt")
write(results_koef, "2019_Tot_chl_results_koef.txt")

# the same loop for SPAD values

results_p <- vector()
results_R <- vector()
results_i <- vector()
results_koef <- vector()

for (I in 2159:2188) # change the values of I based on the results od dim function
{
model<-lm(dataVI$SPAD_Cab~dataVI[,I]);
sum=summary(model)
out<-capture.output(sum);
results_p <- append(results_p,grep ("p-value", out, value = TRUE) );
results_R <- append(results_R,grep ("Multiple R-squared", out, value = TRUE) );
results_i <- append(results_i,grep ("(Intercept)", out, value = TRUE) );
results_koef <- append(results_koef,grep ("dataVI", out, value = TRUE) );
}
 
write(results_p, "2019_SPAD_Cab_results_p.txt")
write(results_R, "2019_SPAD_Cab_results_R.txt")
write(results_i, "2019_SPAD_Cab_results_i.txt")
write(results_koef, "2019_SPAD_Cab_results_koef.txt")

