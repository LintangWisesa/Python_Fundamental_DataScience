
inputuser = ''
password = '12345678'

while inputuser != password:
    inputuser = input('Ketikkan password : ')
    if inputuser != password:
        print('Password Salah!')
    else:
        print('Password Benar!')
