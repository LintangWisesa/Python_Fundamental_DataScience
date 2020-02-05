ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)
# print(adults)
# print(list(adults))

#############################

z = filter(lambda a: True if a >= 18 else False, ages)
print(list(z))

z = filter(lambda a: a >= 18, ages)
print(list(z))

############################

x = [1, 2, 3, 4, 5, 99]
y = [1, 2, 6, 7, 8, 99]

z = list(filter(lambda a: a in x, y))
print(z)

z = []
for i in y:
  if i in x:
    z.append(i)
print(z)

############################

z = list(filter(lambda x: True if x<3 else False, x))
print(z)

z = list(filter(lambda x: x<3, x))
print(z)