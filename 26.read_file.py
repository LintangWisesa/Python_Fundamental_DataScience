
#  'r'ead  'w'rite  'a'ppend  'r+'read+write

file = open('26.karyawan.txt', 'r')

print(file.readable())        # check if it can be read
# print(file.read())          # read all files
# print(file.readlines())     # read all lines as list
# print(file.readline())      # read first line

for data in file.readlines():
    print(data)

file.close()
