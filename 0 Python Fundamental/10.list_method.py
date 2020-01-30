x = [1,2,3,4,5,6,7,8,9]
y = range(1, 10, 2) # start, stop, step
print(list(y))

# ==========================

angka = [1,2,3,4,5,6]
mobil = ['Avanza', 'Innova', 'Xenia']

mobil.append('Brio')
print(mobil)

mobil.insert(1, 'Pajero')
print(mobil)

mobil.remove('Pajero')  # remove Pajero
# mobil.remove(0)       # remove index ke-0
print(mobil)

mobil.clear()
print(mobil)

angka.pop()
print(angka)

angka.pop(2) # hapus index ke-2
print(angka)

angka.sort()                # sort number value
# angka.sort(reverse=True)  # sort number value descending
print(angka)

angka.reverse()             # membalik index
print(angka)

angka2 = angka.copy()
angka2 = angka[::2].copy()
print(angka2)

angka2[0:2] = [12, 13] 
print(angka2)

mobil.extend(angka)
print(mobil)

# ==============================

a = [0, 2, 4, 'Andi']
b = [1, 3, 5]

print(a + b)
print(a * 2)

# ==============================

x = [1,2,3]
y = ['a', 'b', 'c']

print(x + y)