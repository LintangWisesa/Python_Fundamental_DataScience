# mean square error a.k.a cost function
# y = mx + b

import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

def gradien(x,y):
    m_curr = b_curr = 0
    iterasi = 1000
    n = len(x)
    learning_rate = 0.001
    # change iterasi & learning rate!     

    for i in range(iterasi):
        y_predicted = m_curr * x + b_curr
        cost = (1/n)*sum([val**2 for val in (y-y_predicted)])

        md = -(2/n)*sum(x*(y - y_predicted))
        bd = -(2/n)*sum(y - y_predicted)

        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print('m {}, b {}, cost {}, iterasi {}'.format(m_curr, b_curr, cost, i))

# gradien(x,y)

# linear regression
from sklearn.linear_model import LinearRegression
modelLR = LinearRegression()
modelLR.fit(x.reshape(-1,1), y)
print(modelLR.coef_)
print(modelLR.intercept_)