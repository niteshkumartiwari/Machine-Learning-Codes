# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 11:34:49 2017

@author: Jaadugar
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import dataset
dataset= pd.read_csv('50_Startups.csv')
X= dataset.iloc[:,:-1].values
y= dataset.iloc[:,4].values

##Encoding of the categorical variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelEncoder= LabelEncoder()
X[:,3]= labelEncoder.fit_transform(X[:,3])
onehotencoder= OneHotEncoder(categorical_features =[3])
X =onehotencoder.fit_transform(X).toarray()

#Precaution for Dummy variable Trap
X= X[:,1:]

#Splitting Training and Test set
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test= train_test_split(X, y, test_size=0.2, random_state=0)

#Fitting linear Regression model to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

#Predicting 
y_pred= regressor.predict(X_test)

#Building the optimal model using the Backward Elimination
import statsmodels.formula.api as sm
X= np.append(arr= np.ones((50,1)).astype(int), values=X , axis=1)
X_opt=  X[:,[0,1,2,3,4,5]]
regressor_OLS= sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt=  X[:,[0,1,3,4,5]]
regressor_OLS= sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt=  X[:,[0,3,4,5]]
regressor_OLS= sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

X_opt=  X[:,[0,3,5]]
regressor_OLS= sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()