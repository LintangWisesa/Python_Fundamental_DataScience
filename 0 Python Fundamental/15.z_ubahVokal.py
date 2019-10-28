
# misal: dog -> dgg & bird -> bgrd

def translate(kata):
    ubah = ''
    for huruf in kata:
        if huruf in 'aiueo':
            ubah = ubah + 'g'
        else:
            ubah = ubah + huruf
    return ubah

print(translate('lintang'))
# print(translate(input('Ketik kalimat: ')))


def translate2(kata):
    ubah = ''
    for huruf in kata:
        if huruf.lower() in 'aiueo':
            if huruf.isupper():
                ubah = ubah + 'G'
            else:
                ubah = ubah + 'g'
        else:
            ubah = ubah + huruf
    return ubah

print(translate2(input('Ketik kalimat: ')))
