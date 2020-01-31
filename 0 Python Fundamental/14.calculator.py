no1 = float(input('Masukkan angka 1 : '))
op = input('Masukkan operator : ( + - * / ) ')  #  +  -  *  /
no2 = float(input('Masukkan angka 2 : '))

if op == '+':
    print(no1 + no2)
elif op == '-':
    print(no1 - no2)
elif op == '/':
    print(no1 / no2)
elif op == '*':
    print(no1 * no2)
else:
    print('Maaf, operator tidak dikenali!')

# =======================================

angka = input('Silakan ketik angka: ')

if angka.isdigit():
    if int(angka) % 2 == 0:
        print('Angka', angka, 'tergolong GENAP')
    else:
        print('Angka', angka, 'tergolong GANJIL')
else:
    print('Maaf input Anda tidak valid')

# ==========================================

a1 = float(input('Ketik angka 1 : '))
op = input('Ketik operator ( + - x / ) : ')
a2 = float(input('Ketik angka 2 : '))

if op == '+':
    print(f'{a1} {op} {a2} = {a1 + a2}')
elif op == '-':
    print(f'{a1} {op} {a2} = {a1 - a2}')
elif op == '*':
    print(f'{a1} {op} {a2} = {a1 * a2}')
else:
    print(f'{a1} {op} {a2} = {a1 / a2}')