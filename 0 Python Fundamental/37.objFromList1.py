x = {
    'kota': 'Jakarta', 
    'prodi': 'Teknik SIpil', 
    'alamat': 'BSD'
    }

# 1. create class
# 2. turn dict to obj

class test:
    def __init__(self, kota, prodi, alamat):
        self.kota = kota
        self.prodi = prodi
        self.alamat = alamat

x = test(x['kota'], x['prodi'], x['alamat'])
print(x.kota)
print(x.prodi)
print(x.alamat)