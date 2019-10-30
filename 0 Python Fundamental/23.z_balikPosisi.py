
a = [1,2,3,4]
a.reverse()
print(a)

b = [5,6,7,8]
print(b[::-1])

c = [9,10,11,12]
print(list(reversed(c)))

# ===================================

def balikPosisi(arr):
    y = []
    for i in range(len(arr)):
        y.insert(0, arr[i])
    return y
x = [1, 2, 3, 4, 5, 6, 7]
y = ['Andi', 'Budi', 'Caca']
print(balikPosisi(x))
print(balikPosisi(y))

# ===================================

def balikPosisi(arr):
    for i in range(round(len(arr)/2)):
        tempArr = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = tempArr
    return arr

print(balikPosisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikPosisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikPosisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))
