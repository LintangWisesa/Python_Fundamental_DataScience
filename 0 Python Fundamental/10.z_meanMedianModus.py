x = [2, 3, 5, 7, 1, 2, 5, 7, 4, 6, 9, 5, 5, 3, 3, 3]

# ========================
# MEAN
mean = sum(x) / len(x)
print(mean)

# ========================
# MEDIAN
x.sort()
print(x)
if len(x) % 2 != 0:
    median = x[len(x)//2]   # x[round(len(x)/2)-1]
    print(median)
else:
    i = (len(x) + 1) // 2
    median = (x[i] + x[i+1]) / 2
    print(median)

# ========================
# MODUS
y = set(x)
y = list(y)
print(x)
print(y)

count = []
for i in y:
    c = 0
    for j in x:
        if j == i:
            c += 1
    count.append(c)
print(count)
