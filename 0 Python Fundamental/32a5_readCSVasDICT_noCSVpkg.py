# read csv as dict without csv package

myfile = open('32a4.csv', 'r')

data = []
for i in myfile.readlines()[1:]:
    no = int(i.split(';')[0])
    nama = i.split(';')[1].replace('\n','')
    x = {'no': no, 'nama': nama}
    data.append(x)
print(data)