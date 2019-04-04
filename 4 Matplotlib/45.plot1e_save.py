
import matplotlib.pyplot as plt 
import numpy as np 
a = [1,2,3,4,5,6,7,8,9]
a = np.array(a)

plt.plot(a,a,'g--', a,a**2,'r--', a,a**3,'b--')

plt.title('Ujicoba Visualisasi Data')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.grid(True)
plt.legend(['a x a', 'a x aa', 'a x aaa'])

plt.savefig('45.plot1e.png')
plt.show()