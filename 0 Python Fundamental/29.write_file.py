
# 'a' append : add element to the end of the file
# 'w' write : overwrite the entire file or create a new file

file = open('26.karyawan.txt', 'a')
file.write('\nEuis - Staf Marcomm')
file.close()

# file = open('26.karyawan.txt', 'w')
file = open('27.index.html', 'w')
file.write('<h1>Tes Create HTML from Python!</h1>')
file.close()