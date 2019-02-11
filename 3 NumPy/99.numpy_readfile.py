
import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('99.data.txt', delimiter=',', unpack=True)
# np.loadtxt bisa jg dipakai utk CSV

plt.plot(x, y, label='Data dari file')
plt.title('Tes Plotting Data')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.legend()
plt.show()