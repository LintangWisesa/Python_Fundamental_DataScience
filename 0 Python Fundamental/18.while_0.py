i = 1
while i <= 10:
    print(i)
    i += 1      # artinya i = i + 1

print('Looping selesai!')

# ================

angka = [11, 22, 23, 24, 25, 26, 27]
i = 0
while i <= len(angka)-1:
    print(angka[i])
    i += 1

# ================

angka = [11, 22, 23, 24, 25, 26, 27]
angka2 = []
i = 0
while i <= len(angka)-1:
    angka2.append(angka[i] * 2)
    i += 1

print(angka)
print(angka2)
