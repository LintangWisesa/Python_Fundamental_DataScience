import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

sb.set()    # atau:   plt.style.use('seaborn')

x = np.arange(10)
y = np.arange(10)
plt.plot(x, y)
plt.show()