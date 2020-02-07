# read csv as dict without csv package

myfile = open('32a4.csv', 'r')
data = []
for i in myfile.readlines()[1:]:
    no = int(i.split(';')[0])
    nama = i.split(';')[1].replace('\n','')
    x = {'no': no, 'nama': nama}
    data.append(x)
# print(data)

# user input
nama = input('Ketik nama : ')
new = {'no': data[-1]['no'] + 1, 'nama': nama}
data.append(new)

myfile = open('32a4.csv', 'w')
myfile.write('no;nama\n')

myfile = open('32a4.csv', 'a')
for i in data:
    myfile.write(f'{i["no"]};{i["nama"]}\n')