import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig, [ax1, ax2] = plt.subplots(1,2)  # row, col
ax1.plot([1,2,3], [3,2,5])
ax2.plot([1,2,3], [3,2,5])

plt.show()