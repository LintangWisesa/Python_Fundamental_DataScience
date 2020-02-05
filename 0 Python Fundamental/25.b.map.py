
# MAP: menerapkan suatu function thd tiap elemen dalam iterable value

x = [1, 2, 3, 4, 5]

def jumlah(i):
    return i + i
y = map(jumlah, x)
print(list(y))

z = map(lambda a: a + a, x)
print(list(z))

#################################

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

def jumlah(i, j):
    return i + j

z = map(jumlah, x, y)
print(list(z))

##################################

def addition(n): 
    return n + n 
  
# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 

#######################################

a = ['Cokelat', 'Melon', 'Nangka']
b = ['Apel', 'Jeruk', 'Nanas']
def combi(a, b):
    return a+' '+b
x = map(combi, a, b)
# print(x)
# print(list(x))

########################################

x = [2, 4, 6, 8, 10]

def pangkat2(a):
    return a ** 2
# y = map(pangkat2, x)
# print(list(y))

y = map(lambda x : x ** 2, x)
# print(list(y))

# out: [4, 16, 36, 64, 100]

######################################

z = list(map(pow, [2, 3], [2, 3]))
print(z)

a = [1,2,3,4,5]
b = [2,3,2,3,2]
z = list(map(pow, a, b))
print(z)