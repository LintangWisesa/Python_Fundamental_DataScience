
import matplotlib.pyplot as plt 
import numpy as np 
a = [1,2,3,4,5,6,7,8,9]
a = np.array(a)
b = [1,4,9,3,5,8,4,2,5]

plt.plot(a,a,'g--', a,a**2,'r--', a,a**3,'bs', a,a**3,'y--')

plt.xticks(rotation = 90)
# plt.xticks(np.arange(6), list('abcdef'))
# plt.xticks([])
plt.yticks(np.arange(0, 730, step=200))
# plt.yticks(np.arange(0, 10, step=1), rotation=180)

plt.title('Ujicoba Visualisasi Data')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.grid(True)
plt.legend(['a x a', 'a x aa', 'a x aaa'])
plt.show()