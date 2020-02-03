# program dlm func harus indented/menjorok (di-TAB!)

def halo():
    print('Halo semua!')

halo()

# parameter

def hai(nama):
    print('Halo ' + nama)

hai('Ali')

# callback function 

def tes(nama):
    print('Halo', nama)

tes('Andi')
tes(input('Ketik nama:'))

# multiple param

def aloha(nama, usia):
    print('Aloha ' + nama + str(usia))

aloha('Zaza', 80)