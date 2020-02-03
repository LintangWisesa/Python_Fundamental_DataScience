# ======================================
# DENGAN WHILE LOOP

inputuser = ''
password = '12345678'

while inputuser != password:
    inputuser = input('Ketikkan password : ')
    if inputuser != password:
        print('Password Salah!')
    else:
        print('Password Benar!')

# ======================================
# DENGAN RECURSIVE FUNCTION

inputuser = ''
password = '12345678'

def inputpass():
    inputuser = input('Ketik password : ')
    if inputuser == password:
        print('Password benar!')
    else:
        print('Password salah!')
        inputpass()

inputpass()