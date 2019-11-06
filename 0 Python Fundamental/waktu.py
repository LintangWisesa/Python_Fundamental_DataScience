
import datetime as dt
x = dt.datetime.now()
listHari = {
    'Monday': 'Senin',
    'Tuesday': 'Selasa',
    'Wednesday': 'Rabu',
    'Thursday': 'Kamis',
    'Friday': 'Jum\'at',
    'Saturday': 'Sabtu'
}
listBulan = {
    'January': 'Januari',
    'February': 'Februari',
    'March': 'Maret',
    'April': 'April',
    'May': 'Mei',
    'June': 'Juni',
    'July': 'Juli',
    'August': 'Agustus',
    'September': 'September',
    'October': 'Oktober',
    'November': 'November',
    'December': 'Desember'
}

class nowTime:
    def __init__(self):
        self.tanggal = x.strftime('%d')
        self.tahun = x.strftime('%Y')
        self.jam = x.strftime('%H')
        self.menit = x.strftime('%M')
        self.detik = x.strftime('%S')
        self.hari = listHari[x.strftime('%A')]
        self.bulan = listBulan[x.strftime('%B')]

waktu = nowTime()