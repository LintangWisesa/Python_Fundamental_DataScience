
import matplotlib.pyplot as plt 
import numpy as np 
a = [1,2,3,4,5,6,7,8,9]
a = np.array(a)
b = [1,4,9,3,5,8,4,2,5]

# - : line
# -- : dash 
# o : point
# s : square
# ^ : segitiga
# * : star
# . : dot
# g: green, b: blue, r: red, y: yellow
# warna dg hexcode: #FF0000, #00FF00, #000000 dst

plt.plot(a,a,'g--', a,a**2,'r--', a,a**3,'bs', a,a**3,'y--')
# plt.plot(a,a,'g-o', a,a**2,'r-*', a,a**3,'bs', a,a**3,'y-^')

plt.title('Ujicoba Visualisasi Data')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.grid(True)
plt.legend(['a x a', 'a x aa', 'a x aaa'])
plt.show()