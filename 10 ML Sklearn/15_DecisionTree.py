
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame([
    {'kantor':'google', 'job':'sales', 'titel':'S1', 'gaji>50jt':0},
    {'kantor':'google', 'job':'sales', 'titel':'S2', 'gaji>50jt':0},
    {'kantor':'google', 'job':'manager', 'titel':'S1', 'gaji>50jt':1},
    {'kantor':'google', 'job':'manager', 'titel':'S2', 'gaji>50jt':1},
    {'kantor':'google', 'job':'staf', 'titel':'S1', 'gaji>50jt':0},
    {'kantor':'google', 'job':'staf', 'titel':'S2', 'gaji>50jt':1},
    {'kantor':'tesla', 'job':'sales', 'titel':'S2', 'gaji>50jt':0},
    {'kantor':'tesla', 'job':'staf', 'titel':'S1', 'gaji>50jt':0},
    {'kantor':'tesla', 'job':'manager', 'titel':'S1', 'gaji>50jt':0},
    {'kantor':'tesla', 'job':'manager', 'titel':'S2', 'gaji>50jt':1},
    {'kantor':'facebook', 'job':'sales', 'titel':'S1', 'gaji>50jt':1},
    {'kantor':'facebook', 'job':'sales', 'titel':'S2', 'gaji>50jt':1},
    {'kantor':'facebook', 'job':'staf', 'titel':'S1', 'gaji>50jt':1},
    {'kantor':'facebook', 'job':'staf', 'titel':'S2', 'gaji>50jt':1},
    {'kantor':'facebook', 'job':'manager', 'titel':'S1', 'gaji>50jt':1},
    {'kantor':'facebook', 'job':'manager', 'titel':'S2', 'gaji>50jt':1}
])
# print(df)

# =====================================

# data target (df['gaji>50jt'])
target = df['gaji>50jt']

# data independent (df tanpa kolom 'gaji>50jt')
inputs = df.drop('gaji>50jt', axis='columns')
print(inputs)

# =====================================
# label encoder: ubah data mjd angka

from sklearn.preprocessing import LabelEncoder
le_kantor = LabelEncoder()
le_job = LabelEncoder()
le_titel = LabelEncoder()

inputs['kantor_n'] = le_kantor.fit_transform(inputs['kantor'])
inputs['job_n'] = le_kantor.fit_transform(inputs['job'])
inputs['title_n'] = le_kantor.fit_transform(inputs['titel'])

# drop kolom yg tak terpakai
inputs_n = inputs.drop(['kantor', 'job', 'titel'], axis='columns')
print(inputs_n)

# ===================================
# decision tree

from sklearn import tree
model = tree.DecisionTreeClassifier()
model.fit(inputs_n, target)

# score model accuration
print(model.score(inputs_n, target))

# predict data [kantor, job, titel]
# kantor: 0 facebook, 1 tesla, 2 google
# job: 0 manager , 1 sales, 2 staf
# titel: 0 s1, 1 s2

print(model.predict([[0,0,0]]))
print(model.predict([[1,0,0]]))
print(model.predict([[2,0,0]]))

# draw the decision tree raph
# import decision tree graph as .dot file
tree.export_graphviz(
    model.fit(inputs_n, target), 
    out_file='15_DecisionTree.dot',
    feature_names=['kantor_n', 'job_n', 'titel_n'],
    class_names=['<10jt', '>10jt']
)
# go to https://dreampuf.github.io/GraphvizOnline 
# to convert the .dot to .png/.svg/image!