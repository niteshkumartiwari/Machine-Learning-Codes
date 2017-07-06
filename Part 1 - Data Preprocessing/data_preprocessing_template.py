# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#tackling the missing data
"""from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])"""

#Encoding categorical variables
"""from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label_encoder_X=LabelEncoder()
X[:,0]=label_encoder_X.fit_transform(X[:,0])       
onehotEncoder=OneHotEncoder(categorical_features= [0])
X=  onehotEncoder.fit_transform(X).toarray()

label_encoder_y=LabelEncoder()
y=label_encoder_y.fit_transform(y)"""

#Splitting datatsets into test case and train test
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X= StandardScaler()
X_train= sc_X.fit_transform(X_train)
X_test= sc_X.fit(X_test)"""