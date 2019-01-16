
# list = [x,y,z]
# tuple = (x,y,z) no assignment
# set = {x,y,z} no indexing

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