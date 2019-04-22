import datetime as dt 
import numpy as np
import time

# unix time now
unix = time.time()
print(unix)

# convert unix
waktu = dt.datetime.fromtimestamp(unix)
print(waktu)

# convert unix with numpy
dateconv = np.vectorize(dt.datetime.fromtimestamp)
date = dateconv(unix)
print(date)