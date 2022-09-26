
# No 4 Draw Boxplot And Wilcoxon Rank Sum Test

# Create Table

Sample_Product <- c(1, 2, 3, 4, 5, 6, 7, 8)
Company_A <- c(117.1, 121.3, 127.8, 121.9, 117.4, 124.5, 119.5, 115.1)
Company_B <- c(123.5, 125.3, 126.5, 127.9, 122.1, 125.6, 129.8, 117.2)

Data <- data.frame(Sample_Product, Company_A, Company_B)

boxplot(Data$Company_A ~ Data$Sample_Product, ylab = 'Packaging Weight', xlab = 'Sample Product Number', 
        main = 'Weight Of Sample Products From Company A')

boxplot(Data$Company_B ~ Data$Sample_Product, ylab = 'Packaging Weight', xlab = 'Sample Product Number', 
        main = 'Weight Of Sample Products From Company B')

boxplot(cbind(Company_A, Company_B))

wilcox.test(Data$Company_A, Data$Company_B)


