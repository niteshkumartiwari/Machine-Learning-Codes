# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:07:55 2017

@author: Jaadugar
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset= pd.read_csv('myCSV.csv', sep=',')
devices = dataset.iloc[0:8,0]
x=pd.Series([0,1,2,3,4,5,6,7])
y=pd.Series([0,1,2])

#Association Time
aTime1 = dataset.iloc[0:8,1]
aTime2 = dataset.iloc[0:8,2]
aTime3 = dataset.iloc[0:8,3]

ax = plt.subplot(111)
ax.bar(x-0.2, aTime1,width=0.2,color='b',align='center')
ax.bar(x, aTime2,width=0.2,color='g',align='center')
ax.bar(x+0.2, aTime3,width=0.2,color='r',align='center')
plt.xticks(x, devices)
plt.title('Association Time')
plt.xlabel('Devices')
plt.ylabel('Time in sec')
plt.show


#Fetching Time
fTime1 = dataset.iloc[0:8,4]
fTime2 = dataset.iloc[0:8,5]
fTime3 = dataset.iloc[0:8,6]

ax = plt.subplot(111)
ax.bar(x-0.2, fTime1,width=0.2,color='b',align='center')
ax.bar(x, fTime2,width=0.2,color='g',align='center')
ax.bar(x+0.2, fTime3,width=0.2,color='r',align='center')
plt.xticks(x, devices)
plt.title('Fetching Time')
plt.xlabel('Devices')
plt.ylabel('Time in sec')
plt.show



#Opening Time
oTime1 = dataset.iloc[0:8,9]
oTime2 = dataset.iloc[0:8,10]
oTime3 = dataset.iloc[0:8,11]

ax = plt.subplot(111)
ax.bar(x-0.2, oTime1,width=0.2,color='b',align='center')
ax.bar(x, oTime2,width=0.2,color='g',align='center')
ax.bar(x+0.2, oTime3,width=0.2,color='r',align='center')
plt.xticks(x, devices)
plt.title('Opening Time')
plt.xlabel('Devices')
plt.ylabel('Time in sec')
plt.show


#Scanning Time
sTime1 = dataset.iloc[0:8,12]
sTime2 = dataset.iloc[0:8,13]
sTime3 = dataset.iloc[0:8,14]

ax = plt.subplot(111)
ax.bar(x-0.2, sTime1,width=0.2,color='b',align='center')
ax.bar(x, sTime2,width=0.2,color='g',align='center')
ax.bar(x+0.2, sTime3,width=0.2,color='r',align='center')
plt.xticks(x, devices)
plt.title('Scanning Time')
plt.xlabel('Devices')
plt.ylabel('Time in sec')
plt.show

#Power Comparison
pDataset= pd.read_csv('myPower.csv', sep=',')
paTime1 = pDataset.iloc[0:3,1]
paTime2 = pDataset.iloc[0:3,2]
paTime3 = pDataset.iloc[0:3,3]

pRange=pDataset.iloc[0:3,0]

ax = plt.subplot(111)
ax.bar(y-0.2, paTime1,width=0.2,color='b',align='center')
ax.bar(y, paTime2,width=0.2,color='g',align='center')
ax.bar(y+0.2, paTime3,width=0.2,color='r',align='center')
plt.xticks(y, pRange)
plt.title('Power vs Association Time')
plt.xlabel('Power Range in dB')
plt.ylabel('Time in sec')
plt.show




