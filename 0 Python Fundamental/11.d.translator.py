
days = {
    'senin': 'monday', 'selasa': 'tuesday', 'rabu': 'wednesday',
    'kamis': 'thursday', 'jumat': 'friday', 'sabtu': 'saturday',
    'minggu': 'sunday'
}

# id = eng
hari = input('Ketik nama hari : ')
print(f'Bahasa Inggrisnya {hari.upper()} = {days[hari.lower()].upper()}')

# eng => id
hari = input('Write day name : ')
print(f'Bahasa for {hari.upper()} = {list(days.keys())[list(days.values()).index(hari.lower())]}')
