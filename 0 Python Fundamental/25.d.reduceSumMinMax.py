
from functools import reduce
z = [1,2,3,4,5]

asum = reduce(lambda x, y: x + y, z)
print(asum)

amax = reduce(lambda x, y: x if (x > y) else y, z)
print(amax)

amin = reduce(lambda x, y: x if (x < y) else y, z)
print(amin)