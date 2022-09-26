
# No 3 Draw Boxplot And Wilcoxon signed rank test

# Create Table

Child_Number <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
Before_Med <- c(58.35, 44.59, 51.75, 48.12, 65.1, 51.15, 63.3, 57.85, 47.21, 52.83)
After_Med <- c(20.01, 19.09, 19.27, 21.33, 24.14, 20.69, 27.88, 22.36, 20.52, 18.37)

Data <- data.frame(Child_Number, Before_Med, After_Med)

boxplot(Data$Before_Med ~ Data$After, ylab = 'Repetitive Behavior Duration', xlab = 'Children Number', 
        main = 'Repetitive Behavior Observation Before New Medication')

boxplot(Data$After_Med ~ Data$Child_Number, ylab = 'Repetitive Behavior Duration', xlab = 'Children Number', 
        main = 'Repetitive Behavior Observation After New Medication')

boxplot(cbind(Before_Med,After_Med))

wilcox.test(Data$Before_Med, Data$After_Med, paired = TRUE)


