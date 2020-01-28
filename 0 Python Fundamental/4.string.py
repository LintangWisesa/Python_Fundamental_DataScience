print('Jum\'at')
print('Lintang\tWisesa')
print('Lintang\nWisesa')

kata = 'Purwadhika'
print(kata + ' Startup School')

print(kata.lower())
print(kata.upper())
print(kata.islower())
print(kata.isupper())
print(kata.upper().isupper())

print(len(kata))
print(kata[3])
print(kata[0:8])
print(kata[0:len(kata):2])
print(kata.index('dhika'))
print(kata.split('a'))
print(kata.split('a')[1])

z = 'Andi dita'
print(z.replace('di', 'na'))
print(z.replace('di', 'na', 1)) # old, new, count
z = z.replace('a', 'o').replace('i', 'o')
print(z)

# ================================

usia = 21
# Usia saya = 21

print('Usia saya' + str(usia))
print('Usia saya', usia)
print('Usia saya %d' % usia)
print('Usia saya = {}'.format(usia))
print(f'Usia saya = {usia}')

# ================================

nama = 'Budi'
usia = 22

print('Halo saya ' + nama + ' usia ' + str(usia))
print('Halo saya', nama, 'usia', usia)
print('Halo saya %s usia %d' % (nama, usia))
print('Halo saya {} usia {}'.format(nama, usia))
print(f'Halo saya {nama} usia {usia}')

'''
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
'''