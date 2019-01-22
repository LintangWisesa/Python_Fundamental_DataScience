
morse = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..',
    '1': '.____',
    '2': '..___',
    '3': '...__',
    '4': '...._',
    '5': '.....',
    '6': '_....',
    '7': '__...',
    '8': '___..',
    '9': '____.',
    '0': '_____'
}

def ubah(teks):
    if teks.upper() == teks.lower():
        kalimat = teks.split(' / ')
        hasil = ''
        for i in kalimat:
            hasil += list(morse.keys())[list(morse.values()).index(i)] 
        print(hasil)
    else:
        kalimat = teks.lower().replace(' ', '')
        hasil = ''
        for i in kalimat:
            hasil += morse[i] + ' / '
        print(hasil)

ubah(input('Ketik karakter yang akan diubah : '))