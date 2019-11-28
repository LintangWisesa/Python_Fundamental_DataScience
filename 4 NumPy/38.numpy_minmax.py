
import numpy as np

x = [1,2,3,4,5]
y = np.array(x)

print(max(x))
print(min(x))

print(y.max())
print(y.min())
# Location of the max
print('Position of max value: ', np.argmax(y))  
# Location of the min
print('Position of min value: ', np.argmin(y))  