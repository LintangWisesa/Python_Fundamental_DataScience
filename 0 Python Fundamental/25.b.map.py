# map python
def y(a):
    return len(a)
a = ['Andilala', 'Budiman', 'Caca']
x = map(y, a)
# print(x)
# print(list(x))

########################################

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

x = pow(2, 2)
y = pow(3, 3)
print(x)
print(y)

z = list(map(pow, [2, 3], [2, 3]))
print(z)