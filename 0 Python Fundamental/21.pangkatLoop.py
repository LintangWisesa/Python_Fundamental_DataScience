
# Pangkat Function

def pangkat(angka, pangkat):
    hasil = 1
    for i in range(pangkat):
        hasil = hasil * angka
    return hasil

print(pangkat(3, 3))

# ====================================

def pangkat(angka, pangkat):
    hasil = 1
    for i in range(pangkat):
        hasil = hasil * angka
    print(hasil)

pangkat(4, 2)