
# try:
#     angka = int(input('Ketik angka: '))
#     print(angka)
# except:
#     print('Input bukan angka!')

# run & coba inputkan bukan angka

try:
    nilai = 10/0
    angka = int(input('Ketik angka: '))
    print(angka)
except ZeroDivisionError:
    print('Tak bisa dibagi 0!')
except ValueError:
    print('Input bukan angka!')