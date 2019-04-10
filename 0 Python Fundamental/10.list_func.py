angka = [1,2,3,4,5,6]
mobil = ['Avanza', 'Innova', 'Xenia']

mobil.extend(angka)
print(mobil)

mobil.append('Brio')
print(mobil)

mobil.insert(1, 'Pajero')
print(mobil)

mobil.remove('Pajero')
print(mobil)

mobil.clear()
print(mobil)

angka.pop()
print(angka)

angka.pop(2)
print(angka)

angka.sort()
print(angka)

angka.reverse()
print(angka)

angka2 = angka.copy()
print(angka2)

angka2[0:2] = [12, 13] 
print(angka2)

# ==============================

a = [0, 2, 4, 'Andi']
b = [1, 3, 5]

print(a + b)
print(a * 2)
