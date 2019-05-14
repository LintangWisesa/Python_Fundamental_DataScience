import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [
    {'nama':'Andi', 'usia':27, 'gaji':7},
    {'nama':'Budi', 'usia':29, 'gaji':9},
    {'nama':'Caca', 'usia':29, 'gaji':6.1},
    {'nama':'Deni', 'usia':28, 'gaji':6},
    {'nama':'Euis', 'usia':42, 'gaji':15},
    {'nama':'Fafa', 'usia':39, 'gaji':15.5},
    {'nama':'Gaga', 'usia':41, 'gaji':16},
    {'nama':'Hani', 'usia':38, 'gaji':16.2},
    {'nama':'Inge', 'usia':36, 'gaji':15.6},
    {'nama':'Janu', 'usia':35, 'gaji':13},
    {'nama':'Kiki', 'usia':37, 'gaji':13.7},
    {'nama':'Luna', 'usia':26, 'gaji':4.5},
    {'nama':'Mini', 'usia':27, 'gaji':4.8},
    {'nama':'Nana', 'usia':28, 'gaji':5.1},
    {'nama':'Opik', 'usia':29, 'gaji':4.95},
    {'nama':'Peni', 'usia':32, 'gaji':5.3},
    {'nama':'Ququ', 'usia':40, 'gaji':6.5},
    {'nama':'Roni', 'usia':41, 'gaji':6.3},
    {'nama':'Sasa', 'usia':43, 'gaji':6.4},
    {'nama':'Tuti', 'usia':39, 'gaji':8},
    {'nama':'Upik', 'usia':41, 'gaji':8.2},
    {'nama':'Vina', 'usia':43, 'gaji':5.8}
]

df = pd.DataFrame(data)

# ============================
# plot dataframe

# plt.scatter(df['usia'], df['gaji']) 
# plt.xlabel('Usia')
# plt.ylabel('Gaji')
# plt.show()

# =============================

from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)

# training
model.fit(df[['usia', 'gaji']])

# prediction
print(model.predict(df[['usia', 'gaji']]))

# or training & prediction at once!
y_predicted = model.fit_predict(df[['usia', 'gaji']])
print(y_predicted)

# ========================

# df['cluster'] = model.predict(df[['usia']])
df['cluster'] = y_predicted

print(df.head())

df0 = df[df['cluster'] == 0]
df1 = df[df['cluster'] == 1]
df2 = df[df['cluster'] == 2]

plt.scatter(df0['usia'], df0['gaji'], color='r')
plt.scatter(df1['usia'], df1['gaji'], color='g')
plt.scatter(df2['usia'], df2['gaji'], color='b') 

plt.xlabel('Usia')
plt.ylabel('Gaji')
plt.show()

# ====================

# centroids
print(model.cluster_centers_)

# plot centroids
plt.scatter(
    model.cluster_centers_[:,0],
    model.cluster_centers_[:,1],
    color = 'y',
    marker = '*',
    s = 150
)

# plot df0, df1, df2
df0 = df[df['cluster'] == 0]
df1 = df[df['cluster'] == 1]
df2 = df[df['cluster'] == 2]
plt.scatter(df0['usia'], df0['gaji'], color='r')
plt.scatter(df1['usia'], df1['gaji'], color='g')
plt.scatter(df2['usia'], df2['gaji'], color='b') 

plt.xlabel('Usia')
plt.ylabel('Gaji')
plt.show()

# ===============================
# decide k / n_cluster with elbow method
# sse = sum of squared error

k_range = range(1,10)
sse = []
for k in k_range:
    model = KMeans(n_clusters = k)
    model.fit(df[['usia', 'gaji']])
    sse.append(model.inertia_)

print(sse)

# plot sse
plt.plot(k_range, sse)
plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.show()