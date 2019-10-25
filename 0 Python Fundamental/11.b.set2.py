
# list = [x,y,z]
# tuple = (x,y,z) immutable, no assignment
# set = {x,y,z} no indexing, like set on math (himpunan)

# 1. Sets are unordered.
# 2. Set elements are unique. Duplicate elements are not allowed.
# 3. A set itself may be modified, but the elements contained in the set must be of an immutable type.
# (elemen set tidak bisa berupa list & dictionary), tuple bisa krn immutable)

# ===============================
# UNION = all elements on set (gabungan)

x = {1, 2, 3}
y = {4, 2, 6}
z = {1, 3, 5}
print(x | y)
print(x | z)
print(x | y | z)

print(x.union(y))
print(y.union(x))
print(x.union(y, z))

# ===============================
# INTERSECTION = elements between sets (irisan)

print(x & y)
print(x & z)
print(x & y & z)

print(x.intersection(y))
print(y.intersection(x))
print(x.intersection(y, z))

# ===============================
# DIFFERENCE = elements only on a sets (selisih)

# only on x
print(x - y)
print(x - z)
print(x - y - z)

# only on x
print(x.difference(y))
print(y.difference(x))
print(x.difference(y, z))

# ===============================
# SYMMETRIC DIFFERENCE

print(x ^ y)
print(x ^ z)
print(x ^ y ^ z)

print(x.symmetric_difference(y))
print(y.symmetric_difference(x))
print(x.symmetric_difference(y, z))

# soal:
# https://brainly.co.id/tugas/7707409
# https://brainly.co.id/tugas/12307211