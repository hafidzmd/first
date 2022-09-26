 
# No 2 Spearman Rank Correlation

# Create Table

GNP_X <- c(2360, 340 ,780, 940, 1120, 1940, 7750, 2520, 16090, 240)
LE_Y <- c(65, 59, 62, 64, 66, 74, 74, 71, 76, 47)

Data <- data.frame(GNP_X, LE_Y)

cor.test(Data$GNP_X, Data$LE_Y,  method = "spearman", exact = FALSE)



