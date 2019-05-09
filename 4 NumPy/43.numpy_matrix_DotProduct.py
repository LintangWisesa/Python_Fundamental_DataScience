
# dot product
# syarat: jumlah kolom matrix a = jumlah baris matrix b

# |1|   
# |2| . | 4 5 6 | = (1x4)+(2x5)+(3x6) = 32 
# |3|   

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a.dot(b))
print(a@b)