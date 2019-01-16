mass = float(input('Masukkan massa tubuh (kg) : '))
height = float(input('Masukkan tinggi badan (cm) : '))
imt = mass / ((height/100) ** 2)

if imt < 18.5:
    print('Massa', mass, 'kg & tinggi', height, 'cm')
    print('IMT =', imt, ': BB Kurang!')
elif imt >= 18.5 and imt < 24.9:
    print('Massa', mass, 'kg & tinggi', height, 'cm')
    print('IMT =', imt, ': BB Ideal!')
elif imt >= 24.9 and imt < 29.9:
    print('Massa', mass, 'kg & tinggi', height, 'cm')
    print('IMT =', imt, ': BB Berlebih!')
elif imt >= 29.9 and imt < 39.9:
    print('Massa', mass, 'kg & tinggi', height, 'cm')
    print('IMT =', imt, ': BB Sangat Berlebih!')
else:
    print('Massa', mass, 'kg & tinggi', height, 'cm')
    print('IMT =', imt, ': BB Obesitas!')