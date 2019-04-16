x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#######################################

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))



# beda lambda & tanpa lambda

def yy(a):
    return a
def xx(a):
    print(yy(a))
xx(12)

# ========================== 

def zz():
    return lambda c : c
b = zz()
print(b(13))