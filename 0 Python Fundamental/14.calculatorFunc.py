def calc():
    x = float(input('Masukkan angka 1 : '))
    op = input('Masukkan operator ( + - * / ) : ')  #  +  -  *  /
    y = float(input('Masukkan angka 2 : '))
    
    if op == '+':
        print(x + y)
    elif op == '-':
        print(x - y)
    elif op == '/':
        print(x / y)
    elif op == '*':
        print(x * y)
    else:
        print('Maaf, operator tidak dikenali!')

calc()