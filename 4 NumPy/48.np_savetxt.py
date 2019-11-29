
import numpy as np
x = y = z = np.arange(0.0,5.0,1.0)

np.savetxt('48a.csv', x, delimiter=',')   # X is an array
np.savetxt('48b.csv', (x,y,z))   # x,y,z equal sized 1D arrays
np.savetxt('48c.csv', x, fmt='%1.4e')   # use exponential notation
np.savetxt('48d.csv', x, fmt='%d', header='nomor', delimiter=',')

# more than 1 column csv
a = np.array(list(map(lambda a, b, c: [a, b, c], x, y, z)))
print(a)
np.savetxt('48e.csv', a, fmt='%d', comments='', 
    header='nilai_X,nilai_Y,nilai_Z', delimiter=','
    )