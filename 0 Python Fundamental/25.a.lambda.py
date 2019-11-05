x = lambda a : a
def y(a):
    return a

print(x(2))
print(y(4))

#######################################

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#######################################

def myFunction(x):
    return lambda a : a ** x

pangkat2 = myFunction(2)
pangkat3 = myFunction(3)
pangkat5 = myFunction(5)

print(pangkat2(2))
print(pangkat3(2))
print(pangkat5(2))

#########################################

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#########################################

x = lambda a : True if a % 2 == 0 else False
def y(a):
    if a % 2 == 0:
        return True
    else:
        return False
print(x(4))
print(y(4))