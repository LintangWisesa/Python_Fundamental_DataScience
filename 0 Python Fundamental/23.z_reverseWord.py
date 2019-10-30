x = 'halo hai'

def reverseWord(kalimat):
    output = []
    kalimat = kalimat.split(' ')
    for kata in kalimat:
        output.append(kata[::-1])
    output = ' '.join(output)
    return output

print(reverseWord(x))