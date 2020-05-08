
# Stdev = Merupakan jarak rata-rata dari mean.
import numpy as np

d = [11, 11, 12, 13, 14]
d = np.array(d)

# hitung manual
meanD = np.mean(d)
sumsel2 = np.sum((d - meanD) ** 2)
stdv = np.sqrt(sumsel2 / (len(d) - 1))
print(stdv)

# hitung numpy
print(np.std(d, ddof=1))