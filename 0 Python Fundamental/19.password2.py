
inputuser = ''
password = '12345678'
tebakanke = 1
batastebakan = 5
melebihibatas = False

while inputuser != password and not melebihibatas:
    if tebakanke <= batastebakan:
        inputuser = input('Ketikkan password : ')
        if inputuser != password and tebakanke < 5:
            tebakanke += 1
            print('Password Salah! Silakan percobaan ke-', tebakanke)
        elif inputuser != password and tebakanke == 5:
            tebakanke += 1
            print('Password Salah! Kesempatan habis!') 
        else:
            print('Selamat! Password Benar!')
    else:
        melebihibatas = True
        print('Mohon maaf, coba lagi lain kali.')
