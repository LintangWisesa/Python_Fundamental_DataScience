
# faktorial loop

def faktorial(x):
    angka = 1
    for i in range(1, x+1):
        angka *= i
    return angka

print(faktorial(2))
print(faktorial(3))
print(faktorial(5))