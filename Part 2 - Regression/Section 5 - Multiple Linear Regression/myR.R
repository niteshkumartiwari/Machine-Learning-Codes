dataset= read.csv('50_Startups.csv')

dataset$State=factor(x=dataset$State,
                     levels = c('New York','California','Florida'),
                     labels = c(1,2,3))

library(caTools)
set.seed(123)
split= sample.split(dataset$Profit, SplitRatio = 0.8)
training_set= subset(dataset, split==TRUE)
test_set= subset(dataset, split==FALSE)

regressor=lm(formula = Profit ~ .,
             data = training_set)

summary(regressor)

regressor=lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
             data = training_set)
summary(regressor)

regressor=lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend,
             data = training_set)
summary(regressor)

regressor=lm(formula = Profit ~ R.D.Spend + Administration ,
             data = training_set)
summary(regressor)