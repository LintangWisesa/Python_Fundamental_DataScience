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

angka.sort()
print(angka)

angka.reverse()
print(angka)

angka2 = angka.copy()
print(angka2)