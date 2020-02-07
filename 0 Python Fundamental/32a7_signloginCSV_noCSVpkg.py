# read csv as dict without csv package

myfile = open('32a4.csv', 'r')
data = []
for i in myfile.readlines()[1:]:
    no = int(i.split(';')[0])
    nama = i.split(';')[1].replace('\n','')
    x = {'no': no, 'nama': nama}
    data.append(x)
# print(data)

# signup!
def signup():
    nama = input('Ketik nama : ')
    no = data[-1]['no'] + 1
    new = {'no': no, 'nama': nama}
    data.append(new)
    myfile = open('32a4.csv', 'w')
    myfile.write('no;nama\n')
    myfile = open('32a4.csv', 'a')
    for i in data:
        myfile.write(f'{i["no"]};{i["nama"]}\n')
    print(f'Anda terdaftar dengan no = {no}')

# login
def login():
    nama = input('Ketik nama : ')
    no = int(input('Ketik no : '))
    x = {'no':no, 'nama':nama}
    if x in data:
        print('Sukses Login!')
    else:
        print('Gagal Login!') 

# mulai program
def start():
    print('Welcome! pilih opsi:')
    print('1. Signup / Registrasi peserta')
    print('2. Login / Masuk akun peserta')
    opsi = int(input('Ketik opsi pilihan (1/2) : '))
    if opsi == 1:
        signup()
    elif opsi == 2:
        login()
    else:
        print('Maaf, hanya masukkan 1 / 2')
        start()

start()