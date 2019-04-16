
# 'a' append : add element to the end of the file
# 'w' write : overwrite the entire file or create a new file

file = open('28.karyawan.txt', 'a')
file.write('\nEuis - Staf Marcomm')
file.close()

# file = open('26.karyawan.txt', 'w')
file = open('27.index.html', 'w')
file.write('<h1>Tes Create HTML from Python!</h1>')
file.close()

# create a python file
file = open('13.py', 'w')
file.write('print(\'Halo 1!\')\n')
file.write('print(\'Halo 2!\')')