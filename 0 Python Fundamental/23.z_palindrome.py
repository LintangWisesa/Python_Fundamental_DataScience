
# cara 1
def palindrome(kata):
    y = []
    for i in list(kata):
        y.insert(0, i)
    if ''.join(y) == kata:
        return True
    else:
        return False

print(palindrome('katak'))
print(palindrome('malam'))
print(palindrome('oppo'))

# ================================

# cara 2
# print(''.join(list(reversed('kata'))))

kata = 'katak'
def palindrome(kata):
    if ''.join(list(reversed(kata))) == kata:
        return True
    else:
        return False
print(palindrome(kata))

# sama dgn yg di atas:

kata = 'katak'
def palindrome(kata):
    if kata[::-1] == kata:
        return True
    else:
        return False
print(palindrome(kata))

# =================================

# cara 3
kata = 'katak'
def palindrome(kata):
    for i in range(round(len(kata)/2)):
        palindromekah = False
        if kata[i] == kata[len(kata)-1-i]:
            palindromekah = True
        else:
            palindromekah = False
            break
    return palindromekah

print(palindrome('malam'))
print(palindrome('apa'))