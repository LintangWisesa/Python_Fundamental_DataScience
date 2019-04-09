# input string

input('Are you ready? : ')
nama = input('Ketik nama Anda: ')
usia = input('Ketik usia Anda: ')
print('Halo ' + nama + '! Anda ' + usia)

# access 1st input

nama = input('Halo, namamu siapa? : ')
usia = input('Halo ' + nama + '! usiamu berapa? : ')

print('Hai', nama, 'usia Anda', usia, 'th')

# input number

angka = input('Ketik angka : ')
kuadrat = str(pow(int(angka), 2))
print('Kuadrat dari ' + angka + ' = ' + kuadrat)