
def pangkat(x,y):
    if (y == 1):
        return x
    else:
        return x * pangkat(x, y-1)

print(pangkat(2,3))
print(pangkat(3,3))
print(pangkat(10,5))