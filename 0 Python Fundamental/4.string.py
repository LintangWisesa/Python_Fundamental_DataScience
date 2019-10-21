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
print(kata.replace('dhika', 'caraka'))

print(kata.split('a'))
print(kata.split('a')[1])

# ================================

usia = 21
# Usia saya = 21

print('Usia saya' + str(usia))
print('Usia saya', usia)
print('Usia saya %d' % usia)
print('Usia saya = {}'.format(usia))
print(f'Usia saya = {usia}')