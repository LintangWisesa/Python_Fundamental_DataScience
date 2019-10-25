
days = {
    'senin': 'monday', 'selasa': 'tuesday', 'rabu': 'wednesday',
    'kamis': 'thursday', 'jumat': 'friday', 'sabtu': 'saturday',
    'minggu': 'sunday'
}

hari = list(days)
day = list(days.values())
# print(hari)
# print(day)

name = input('Ketik nama hari (ENG/IDN) : ')

if name.lower() in hari:
    print(f'Bahasa Inggris {name.upper()} adalah {days[name.lower()].upper()}')
else:
    print(f'Bhs. Indonesia {name.upper()} adalah {hari[day.index(name.lower())]}')

