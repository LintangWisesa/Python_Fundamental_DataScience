
def ganjilGenap(angka):
    if angka % 2 == 0:
        return 'Angka '+str(angka)+' tergolong GENAP'
    else:
        return 'Angka '+str(angka)+' tergolong GANJIL'

print(ganjilGenap(12))