
import matplotlib.pyplot as plt 
import numpy as np 

a = [1,2,3,4,5,6,7,8,9]
a = np.array(a)

plt.plot(a,a, a,a**2, a,a**3)
plt.title('Ujicoba Visualisasi Data')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.grid(True)
plt.legend(['a x a', 'a x aa', 'a x aaa'], loc = 3)
plt.show()

# legend location (loc) code
# 'best'	        0
# 'upper right'	    1
# 'upper left'	    2
# 'lower left'	    3
# 'lower right'	    4
# 'right'	        5
# 'center left'	    6
# 'center right'    7
# 'lower center'    8
# 'upper center'    9
# 'center'	        10