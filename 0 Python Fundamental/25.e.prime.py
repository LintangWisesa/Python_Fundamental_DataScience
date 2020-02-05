
# prime function

def prima(x):
    if x > 1:
        if x == 2: 
            return True
        else:
            for i in range(2, x):
                if x % i == 0: 
                    return False
            return True
    else: 
        return False

print(prima(81))

z = list(filter(prima, range(10)))
print(z)

######################################

z = list(filter(lambda x: x>1 and x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0 or x in [2, 3, 5], range(101)))
print(len(z))
print(z)