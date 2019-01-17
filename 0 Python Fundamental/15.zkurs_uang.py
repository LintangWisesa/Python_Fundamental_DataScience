
datakurs = {
    'USD-IDR': 14000,
    'IDR-USD': 0.00007,
}

def konversi(nilai, metode):
    if metode == 'USD-IDR':
        kurs = datakurs[metode]
        print('USD', nilai, 'setara = IDR', nilai * kurs)
    elif metode == 'IDR-USD':
        kurs = datakurs[metode]
        print('IDR', nilai, 'setara = USD', nilai * kurs)
    else:
        print('Mohon maaf, hanya melayani USD <=> IDR')

konversi(2, 'USD-IDR')
konversi(200000, 'IDR-USD')
konversi(3, 'USD-JPY')