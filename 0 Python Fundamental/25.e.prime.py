
# angka = [1, 2, 3, 4]

# z = list(map(lambda x : x * 2, filter(lambda x: x>3, angka)))
# print(z)

# z = list(filter(lambda x: x>3, map(lambda x : x * 2, angka)))
# print(z)


# z = list(filter(lambda x: x ==  or x % i, range(101)))
# print(z)

# prime function

# def prima(x):
#     if x > 1:
#         if x == 2: 
#             return True
#         else:
#             for i in range(2, x):
#                 if x % i == 0: 
#                     return False
#                 else: 
#                     return True
#     else: 
#         return False

# print(prima(81))

def prime(n):
    count = 0
    for i in range(1, (n+1)): 
         if n % i == 0: 
             count += 1
    if count > 2:
        print("Not a prime")
    else:
        print("A prime")

print(prime(81))

# z = list(filter(prima, range(10)))
# print(z)

##############################

z = list(filter(lambda x: x>1 and x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0 or x in [2, 3, 5], range(101)))
# print(len(z))