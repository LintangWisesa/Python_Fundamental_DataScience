
kawan = ['Andi', 'Budi', 'Caca']

print(kawan)
print(kawan[0])
print(kawan[len(kawan) - 1])
print(kawan[-1])
print(kawan[-2])

kawan[1] = 'Bambang'
print(kawan[0:2])

print(kawan.index('Caca'))
print(kawan.count('Caca'))

print(kawan[0::2])
print(kawan[1::2])
print(kawan[1:3:2]) # list[start:stop:step]
print(kawan[::-1])

print('Andi' in kawan)
print('Andi' not in kawan)