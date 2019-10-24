'''
Di dalam kandang terdapat kambing dan ayam sebanyak 13 ekor. 
Jika jumlah kaki hewan tersebut 32, maka jumlah kambing 
dan ayam masing-masing adalah....
'''

########################################

# x + y = 13
# 4x + 2y = 32

# x = 13 - y
# y = 13 - x

########################################

# 4(13 - y) + 2y = 32
# 52 - 4y + 2y = 32
# 52 - 2y = 32
# 2y = 52 - 32

# ayam = ((4 * totalEkor) - totalKaki) / 2
# kambing = totalEkor - ayam

jmlekor = 13
jmlkaki = 32
kakiA = 2
kakiK = 4

ayam = ((kakiK * jmlekor) - jmlkaki) / 2
kambing = jmlekor - ayam
print(f'Jumlah ayam = {ayam}')
print(f'Jumlah kambing = {kambing}')

########################################

# 4x + 2(13 - x) = 32
# 4x + 26 - 2x = 32
# 2x = 32 - 26

# kambing = (totalKaki - (kakiA * totalEkor)) / kakiK
# ayam = totalEkor - kambing

kambing = (jmlkaki - (kakiA * jmlekor)) / 2
ayam = jmlekor - kambing
print(f'Jumlah ayam = {ayam}')
print(f'Jumlah kambing = {kambing}')