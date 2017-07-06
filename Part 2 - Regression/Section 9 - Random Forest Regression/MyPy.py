# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 18:28:49 2017

@author: Jaadugar
"""
#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Import Datasets
dataset= pd.read_csv('Position_Salaries.csv')
X= dataset.iloc[:,1:2].values
y= dataset.iloc[:,2].values

from sklearn.ensemble import RandomForestRegressor
regressor= RandomForestRegressor(n_estimators=3000,random_state=0)
regressor.fit(X, y)

y_pred=regressor.predict(6.5)

X_grid= np.arange(min(X), max(X),0.01)
X_grid=X_grid.reshape((len(X_grid),1))
plt.scatter(X, y, color='blue')
plt.plot(X_grid, regressor.predict(X_grid), color='red')
plt.title('Random Forest')
plt.xlabel('Levels')
plt.ylabel('Salaries')

