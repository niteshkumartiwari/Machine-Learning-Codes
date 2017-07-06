dataset= read.csv('Position_Salaries.csv')
dataset= dataset[2:3]

library(caTools)
line_reg=lm(formula = Salary ~ .,
            data = dataset)

#Fitting polynomial regression to the dataset
dataset$Level2= dataset$Level^2
poly_reg=lm(formula= Salary ~ .,
            data = dataset)

library(ggplot2)

