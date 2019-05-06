# sortit hanya 3 elemen pertama

angka = [14, 2, 34, 12, 67, 2]
print(angka)

jumlahKarakterPertamaYgAkanDisortir = 3
x = angka[0:jumlahKarakterPertamaYgAkanDisortir]
x.sort()
print(x)

angka[0:len(x)] = x
print(angka)

# x.sort(reverse = True)
# print(x)