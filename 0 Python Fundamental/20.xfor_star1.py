
# segitiga siku isi *
star = ''
for i in range(5):
    star += ' * '
    print(star)

# segitiga siku isi angka index
angka = ''
for i in range(5):
    angka = angka + str(i) + ' '
    print(angka)

# segitiga siku isi index sama
for num in range(10):
    for i in range(num):
        print(num, end=" ")
    print("")

# =======================================

# segitiga siku * terbalik
for i in range(5):
    for j in range(5 - i):
        print(' * ', end='')
    print()

# segitiga siku terbalik isi angka
for i in range(5):
    for j in range(5 - i):
        print(str(j)+' ', end='')
    print()