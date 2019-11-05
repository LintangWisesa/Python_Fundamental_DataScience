class student:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

data = [
    {'nama': 'Andi', 'usia': 21},
    {'nama': 'Budi', 'usia': 22},
    {'nama': 'Caca', 'usia': 23},
    {'nama': 'Deni', 'usia': 24}
]

def createObj(x):
    nama = x['nama']
    print(nama)
    vars()[nama] = student(x['nama'], x['usia'])
    return vars()[nama]

x = list(map(createObj, data))

for i in x:
    print(i.nama)

# food = 'roti'
# vars()[food] = 123
# print(roti)
