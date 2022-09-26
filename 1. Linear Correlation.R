
# No 1 Linear Correlation

#Create Table

Rainfall_X <- c(12.3, 13.7, 14.5, 11.2, 13.2, 14.1, 12.0) 
Yield_Y    <- c(6.25, 8.02, 8.42, 5.27, 7.21, 8.71, 5.68)

Data <- data.frame(Rainfall_X, Yield_Y)

cor.test(Data$Rainfall_X, Data$Yield_Y)



