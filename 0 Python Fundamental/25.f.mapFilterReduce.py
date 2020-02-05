
angka = [1,2,3,4,5,6,7,8,9,10]

z = list(filter(lambda x: x>3, map(lambda x : x * 2, angka)))
print(z)
