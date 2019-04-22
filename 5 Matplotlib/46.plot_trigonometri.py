import numpy as np 
import matplotlib.pyplot as plt

w = np.arange(0, 3 * np.pi, 0.1)
x = np.sin(w)
y = np.cos(w)
z = np.tan(w)

plt.plot(w,x,'r--', w, y, 'g-', w,z,'b-')
plt.grid(True)
plt.title('Grafik Trigonometri')
plt.legend(['sinus', 'cosinus', 'tangent'])
plt.show()