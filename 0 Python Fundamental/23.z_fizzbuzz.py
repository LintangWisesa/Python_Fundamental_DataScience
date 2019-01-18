
def fizbuzz(x):
    for i in range(1, x+1):
        if i % 3 == 0 and i % 5 == 0:
            print('Ting')
        elif i % 3 == 0:
            print('Dor')
        elif i % 5 == 0:
            print('Cess')
        else:
            print(i)

fizbuzz(15)