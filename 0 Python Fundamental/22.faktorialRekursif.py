
# recursive function

def faktorial(x):
    if (x <= 2):
        return x
    else:
        return x * faktorial(x-1)

print(faktorial(2))
print(faktorial(3))
print(faktorial(5))

