# tuple is immutable, tak bisa diedit!

posisi = (1,6)
# posisi[0] = 2   -> error! tuple tdk bisa diedit
print(posisi[0])
print(posisi[1])

# list of tuples
tuples = [(1,2), (2,2), (3,4)]
print(tuples[1])
print(1 in tuples[0])
print(1 not in tuples[0])

print(list(tuples))

# ======================================
# keunikan tuple

my_tuple = ("Andi")
print(type(my_tuple))  # <class 'str'>

# Creating a tuple having one element
my_tuple = ("Andi",)  
print(type(my_tuple))  # <class 'tuple'> 

# Parentheses is optional
my_tuple = "Andi",
print(type(my_tuple))  # <class 'tuple'> 

y = "Andi","Budi","Caca"
print(type(y))         # <class 'tuple'>

# ======================================
# exercises

a = ((1, 2), (3, 4), (5, 6), (7, 8))
# print(a[1][1])

# output = ((3, 4), (1, 2), (7, 8), (5, 6))
# c = [a[1], a[0], a[3], a[2]]
# a = tuple(c)
# print(a)

# output = ((4, 3), (2, 1), (6, 5), (8, 7))
# d = [a[1][::-1], a[0][::-1], a[3][::-1], a[2][::-1]]
# a = tuple(d)
# print(a)

# output = ((1, 3), (2, 4), (5, 7), (6, 8))
e = [(a[0][0], a[1][0]), (a[0][1], a[1][1]), (a[2][0], a[3][0]), (a[2][1], a[3][1])]
a = tuple(e)
print(a)

# ======================================
# method

x = (1,2,3)
print(x + x)
print(x * 5)

del x
print(x) # NameError: name 'x' is not defined

# ===========================

x = [
    (1, ['a', 'b']), 
    (3, 4)
]
x[0][1][0] = "Andi"
print(x)