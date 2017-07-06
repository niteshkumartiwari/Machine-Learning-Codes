import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset= pd.read_csv('Mall_Customers.csv')
X= dataset.iloc[:,[3,4]].values

#Using elbow method
from sklearn.cluster import KMeans 
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',n_init=10, max_iter=300, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1, 11), wcss)    
plt.title('Elbow Method')
plt.xlabel('clusters')
plt.ylabel('kMeans')
plt.legend()

kmeans=KMeans(n_clusters=5,init='k-means++',n_init=10, max_iter=300, random_state=0)
y_means=kmeans.fit_predict(X)

plt.scatter(X[y_means==0,0],X[y_means==0,1],c='red',s=100,label='cluster 1')
plt.scatter(X[y_means==1,0],X[y_means==1,1],c='yellow',s=100,label='cluster 2')
plt.scatter(X[y_means==2,0],X[y_means==2,1],c='blue',s=100,label='cluster 3')
plt.scatter(X[y_means==3,0],X[y_means==3,1],c='orange',s=100,label='cluster 4')
plt.scatter(X[y_means==4,0],X[y_means==4,1],c='violet',s=100,label='cluster 5')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
