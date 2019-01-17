datakurs = {
    'USD-IDR': 14000,
    'IDR-USD': 0.00007,
}

def konversi():
    metode = input('Silakan masukkan metode konversi : ')
    nilai = float(input('Silakan masukkan nominal : '))
    if metode == 'USD-IDR':
        kurs = datakurs[metode]
        print('USD', nilai, 'setara = IDR', nilai * kurs)
    elif metode == 'IDR-USD':
        kurs = datakurs[metode]
        print('IDR', nilai, 'setara = USD', nilai * kurs)
    else:
        print('Mohon maaf, hanya melayani USD <=> IDR')

konversi()