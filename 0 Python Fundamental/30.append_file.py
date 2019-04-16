
list = ['Andi', 'Budi', 'Caca']

file = open('30.data.txt', 'a')

for i in list:
    file.write('\n' + i)
