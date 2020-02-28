
import numpy as np

x = [1,2,3,4,5]

print(max(x))
print(min(x))
# location max & min
print(x.index(max(x)))
print(x.index(min(x)))

y = np.array(x)

print(y.max())
print(y.min())
# Location of the max
print('Position of max value: ', np.argmax(y))  
# Location of the min
print('Position of min value: ', np.argmin(y))