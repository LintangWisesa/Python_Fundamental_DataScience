
# - nama benar, pass benar => login
# - nama benar, pass salah => password salah!
# - nama salah             => nama tdk terdaftar!

username = ["Andi", "Budi", "Caca"]
password = ["12345", "8989abc", "098poi"]

user = input('Ketik username : ').capitalize()

if user in username:
    pwd = input('Ketik password : ')
    if pwd == password[username.index(user)]:
        print('Login sukses!')
    else:
        print('Password Salah!')
else:
    print('Nama tidak terdaftar!')