def luasPersegi(sisi):
    return sisi * sisi

print(luasPersegi(6))

hasil = luasPersegi(4)
print(hasil)

# #######################

# return menjadi akhir func, setelah return tidak akan digubris
def x():
    return 'y'
    print('OK')
    print('x')
    print('x')

x()