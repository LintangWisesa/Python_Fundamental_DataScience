# sortir hanya 3 elemen pertama

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

# ===========================
# check duplicates

x = [1, 2, 3, 4, 5, 3]

def duplicates(list, item):
    return [i for i, x in enumerate(lst) if x == item]

print(duplicates(x, 3))
