
import matplotlib.pyplot as plt 
import numpy as np 
a = [1,2,3,4,5,6,7,8,9]
a = np.array(a)
b = [1,4,9,3,5,8,4,2,5]

# LINE STYLE
# - : line
# -- : dash 
# : : dots line
# -. : line dot

# MARKER STYLE: https://matplotlib.org/3.1.1/api/markers_api.html
# o : point
# s : square
# ^ : segitiga
# * : star
# . : dot
# + : plus
# D : diamond
# $lintang$ : text 'lintang'

# g: green, b: blue, r: red, y: yellow, k: black
# warna dg hexcode: #FF0000, #00FF00, #000000 dst
# warna dg nama: grey, gray, lightblue

# 'gs:'  =>  color green, marker square, linesytle .... 
# 'g:s'  =>  color green, marker square, linestyle ....
# 'r*--' =>  color red, marker star, linestyle ---- 

plt.plot(a,a,'g--', a,a**2,'r--', a,a**3,'bs', a,a**3,'y--')
# plt.plot(a,a,'g-o', a,a**2,'r-*', a,a**3,'bs', a,a**3,'y-^')

plt.title('Ujicoba Visualisasi Data')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.grid(True)
plt.legend(['a x a', 'a x aa', 'a x aaa'])
plt.show()