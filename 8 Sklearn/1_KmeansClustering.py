
# unsupervised learning
# membangun centroid di titik terdekat

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# initial data
x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]
# plt.scatter(x,y)
# plt.show()

# create centroids 
X = np.array([[1,2],[5,8],[1.5,1.8],[8,8],[1,0.6],[9,11]])
kmeans = KMeans(n_clusters = 2)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_
print(centroids)
print(labels)

# result & visualization
colors = ['g.', 'r.', 'c.', 'y.']

for i in range(len(X)):
    print('koordinat:', X[i], 'label:', labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=10)
plt.scatter(centroids[:,0], centroids[:,1], marker='x', s=150, linewidth=5, zorder=10)
plt.show()