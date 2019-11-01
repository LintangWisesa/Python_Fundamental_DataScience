
# convert string to date
from datetime import datetime

w = '12/12/19'
x = '12 Apr 2019'
y = '12-04-19 21.45'
z = 'Friday, 12 April 2019'

# ubahStrkeDate = datetime.strptime(w, '%d/%m/%y')
# ubahStrkeDate = datetime.strptime(x, '%d %b %Y')
# ubahStrkeDate = datetime.strptime(y, '%d-%m-%y %H.%M')
ubahStrkeDate = datetime.strptime(z, '%A, %d %B %Y')

print(ubahStrkeDate)
print(type(ubahStrkeDate))
print(ubahStrkeDate.strftime('%A'))

# =======================

b = "Jum'at, 12 April 2019"