import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = plt.figure(1)
x.add_subplot(121) # x.add_subplot(1,2,1)
plt.plot([1,2,3],[4,5,6])

x.add_subplot(122)
plt.plot([1,2,3],[4,5,6])

plt.show()