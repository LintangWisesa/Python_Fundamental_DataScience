import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, median_absolute_error, r2_score

y_true = [10,25,35,55,80]
y_pred = [7,24,41,58,75]

# print(max_error(y_true, y_pred))

print(mean_absolute_error(y_true, y_pred))
# MAE is the easiest to understand, because it's the average error.

print(mean_squared_error(y_true, y_pred))
# MSE is more popular than MAE, because MSE "punishes" larger errors, which tends to be useful in the real world.

print(np.sqrt(mean_squared_error(y_true, y_pred)))
# RMSE is even more popular than MSE, because RMSE is interpretable in the "y" units.
# All of these are loss functions, because we want to minimize them.

print(median_absolute_error(y_true, y_pred))
# MedAE is particularly interesting because it is robust to outliers. The loss is calculated by 
# taking the median of all absolute differences between the target and the prediction.

print(r2_score(y_true, y_pred))
# R2 score represents the proportion of variance (of y) that has been explained 
# by the independent variables in the model. It provides an indication of goodness of 
# fit and therefore a measure of how well unseen samples are likely to be predicted by the model, 
# through the proportion of explained variance.