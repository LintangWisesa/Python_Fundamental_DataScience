
import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('53_data.txt', delimiter=',', unpack=True)

plt.plot(x, y, label='Data dari file')
plt.title('Tes Plotting Data')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.legend()
plt.show()