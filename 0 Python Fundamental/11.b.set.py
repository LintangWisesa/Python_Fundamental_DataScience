
# list = [x,y,z]
# tuple = (x,y,z) immutable, no assignment
# set = {x,y,z} no indexing, like set on math (himpunan)

# 1. Sets are unordered.
# 2. Set elements are unique. Duplicate elements are not allowed.
# 3. A set itself may be modified, but the elements contained in the set must be of an immutable type.
# (elemen set tidak bisa berupa list & dictionary), tuple bisa krn immutable)

x = {1, 2, 3}
y = set([1, 2, 3])
z = set((1, 2, 3))
print(x, type(x))
print(y, type(x))
print(z, type(x))

tes = {1, 2, 'Andi'}
print(type(tes))

# print every element
for elemen in tes:
    print(elemen)
    # print(type(elemen))

# check an element
print(2000 in tes)

# add an element = .add()
tes.add('Budi')
print(tes)

# add elements = .update()
data = [3, 4, 'Caca', 'Deni']
tes.update(data)
tes.update((21, 22))
tes.update({'m', 'n'})
print(tes)

# remove elements = .remove() / if element doesnt exist -> error
tes.remove('Deni')
print(tes)

# remove elements = .discard()
tes.discard('Caca')
print(tes)

# delete all elements
tes.clear()
print(tes)

# delete set
del tes
print(tes)