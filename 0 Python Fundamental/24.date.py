import datetime

x = datetime.datetime.now()

print(x)
print(x.year)

print(x.strftime("%A")) # hari
print(x.strftime("%d")) # tanggal
print(x.strftime("%B")) # bulan full name
print(x.strftime("%m")) # bulan index
print(x.strftime("%Y")) # tahun

print(x.strftime("%H")) # jam sistem 24
print(x.strftime("%I")) # jam sistem 12
print(x.strftime("%p")) # AM/PM
print(x.strftime("%M")) # menit
print(x.strftime("%S")) # detik

print(x.strftime("%c")) # Mon Jan 21 16:45:21 2019
print(x.strftime("%x")) # 01/21/19
print(x.strftime("%X")) # 16:45:49