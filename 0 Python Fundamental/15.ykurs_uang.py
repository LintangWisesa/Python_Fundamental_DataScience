
# konverter Rp IDR <=> $ USD
# nilai = nilai uang yang akan ditukar
# konversi = 'USD-IDR' / 'IDR-USD' 

def konversi(nilai, konversi):
    if konversi == 'USD-IDR':
        kurs = 14000
        print('USD', nilai, 'setara = IDR', nilai * kurs)
    elif konversi == 'IDR-USD':
        kurs = 0.00007
        print('IDR', nilai, 'setara = USD', nilai * kurs)
    else:
        print('Mohon maaf, hanya bisa konversi USD <=> IDR')

konversi(2, 'USD-IDR')
konversi(14000, 'IDR-USD')
konversi(3, 'USD-JPY')