import statistics

# x = [1, 3, 9, 2, 6, 4, 7, 8, 5, 5]
# print(statistics.mean(x)) 
# print(statistics.median(x)) 
# print(statistics.mode(x))

############################################

from functools import reduce

x = [1, 3, 9, 2, 6, 4, 7, 8, 5, 5]

# mean
def rataRata(x):
    x.sort()
    total = reduce(lambda a,b: (a+b), x)
    return total / len(x)
print(rataRata(x))

# median
def nilaiTengah(x):
    x.sort()
    if len(x) % 2 == 0:
        iTengah = [int((len(x)/2)-1), int(len(x)/2)]
    else:
        iTengah = [int(len(x)/2)]
    iTengah = list(map(lambda x: x, iTengah))
    aTengah = list(map(lambda a: x[a], iTengah))
    total = reduce(lambda x, y: (x+y), aTengah)
    return total / len(iTengah)
print(nilaiTengah(x))

# modus
def modus(x):
    x.sort()
    hitung = list(map(lambda a: x.count(a), x)) # jumlah
    iMax = hitung.index(max(hitung))            # index dg jumlah tertinggi
    return x[iMax]
print(modus(x))