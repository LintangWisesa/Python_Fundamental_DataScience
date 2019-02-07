
import requests

listbank = [
    'bca',
    'bi',
    'bjb',
    'bni',
    'bri',
    'btn',
    'bukopin',
    'cimb',
    'commonwealth',
    'danamon',
    'hsbc',
    'jtrust',
    'mandiri',
    'mayapada',
    'maybank',
    'mega',
    'muamalat',
    'ocbc',
    'panin',
    'permata',
    'sinarmas',
    'uob',
    'woorisaudara'
]

def kurs():
    print('Selamat datang')
    print('Silakan pilih konversi yang akan Anda lakukan : ')
    print(' (1) IDR Indonesia => USD United States')
    print(' (2) USD United States => IDR Indonesia')
    print(' (3) USD United States => Bitcoin')
    konversi = input('Pilihan Anda (1/2/3) : ')
    if konversi == '1':
        bank = input('Silakan ketik bank pilihan Anda : ')
        if bank.lower() in listbank:
            url = 'https://kurs.web.id/api/v1/'+bank.lower()
            nominal = input('Silakan input nominal uang yang akan dikonversi : Rp. ')
            data = requests.get(url)
            kursJual = data.json()["jual"]
            kursBeli = data.json()["beli"]
            hasil = int(nominal) / int(kursJual)
            hasil2 = round(hasil, 2)
            print('Hasil konversi Rp', nominal, 'adalah USD', hasil2)
            print('Dengan kurs jual =', kursJual, '& kurs beli =', kursBeli)
        else:
            print('Maaf bank tidak tersedia')
    elif konversi == '2':
        bank = input('Silakan ketik bank pilihan Anda : ')
        if bank.lower() in listbank:    
            nominal = input('Silakan input nominal uang yang akan dikonversi : US$. ')
            data = requests.get(url)
            kursJual = data.json()["jual"]
            kursBeli = data.json()["beli"]
            hasil = int(nominal) * int(kursJual)
            hasil2 = round(hasil, 2)
            print('Hasil konversi US$', nominal, 'adalah Rp.', hasil2)
            print('Dengan kurs jual =', kursJual, '& kurs beli =', kursBeli)
        else:
            print('Maaf bank tidak tersedia')
    elif konversi == '3':
        nominal = input('Silakan input nominal uang yang akan dikonversi : US$. ')
        link = 'https://blockchain.info/tobtc?currency=USD&value='
        data = requests.get(link+nominal).json()
        kursBtc = requests.get(link+'1').json()
        print('Hasil konversi US$', nominal, 'adalah BTC', data)
        print('Dengan kurs US$ 1 =', kursBtc)
    else:
        print('Maaf layanan tidak tersedia')

kurs()