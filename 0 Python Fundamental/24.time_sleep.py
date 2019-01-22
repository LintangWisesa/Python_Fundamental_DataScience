
# import time

# def update():
#     while True:
#         print('Hello World!')
#         time.sleep(1)

# update()

#################################

import time
import datetime

def tes():
    while True:
        x = datetime.datetime.now()
        print(x.strftime('Sekarang jam %H:%M:%S WIB'))
        time.sleep(1)

tes()