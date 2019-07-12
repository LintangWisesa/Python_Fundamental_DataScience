from mlxtend.data import boston_housing_data
X, y = boston_housing_data()

print('Dimensions: %s x %s' % (X.shape[0], X.shape[1]))
print('1st row', X[0])

# Dataset Attributes:
# 1) CRIM per capita crime rate by town
# 2) ZN proportion of residential land zoned for lots over 25,000 sq.ft.
# 3) INDUS proportion of non-retail business acres per town
# 4) CHAS Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
# 5) NOX nitric oxides concentration (parts per 10 million)
# 6) RM average number of rooms per dwelling
# 7) AGE proportion of owner-occupied units built prior to 1940
# 8) DIS weighted distances to five Boston employment centres
# 9) RAD index of accessibility to radial highways
# 10) TAX full-value property-tax rate per $10,000
# 11) PTRATIO pupil-teacher ratio by town
# 12) B 1000(Bk - 0.63)^2 where Bk is the prop. of b. by town
# 13) LSTAT % lower status of the population