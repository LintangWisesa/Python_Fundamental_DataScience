
#  * 
#  *  * 
#  *  *  *
#  *  *  *  *
#  *  *  *  *  *

# segitiga siku isi *
star = ''
for i in range(5):
    star += ' * '
    print(star)

# =============================================

# 1
# 2 2 
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# segitiga siku isi angka
angka = ''
for i in range(5):
    angka = (str(i+1) + ' ') * (i+1)
    print(angka)

# =============================================

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# segitiga siku isi angka index
angka = ''
for i in range(5):
    angka = angka + str(i+1) + ' '
    print(angka)

# =============================================

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# segitiga siku isi index sama
for num in range(10):
    for i in range(num):
        print(num, end=" ")
    print("")

# =============================================

# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

angka = ''
for i in range(5,0,-1):
    angka += str(i) + ' '
    print(angka)