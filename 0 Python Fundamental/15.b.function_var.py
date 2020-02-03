# func dapat memanggil var di luar func
# tp var di dlm func tdk dpt diolah di luar func

x = 99

def halo():
    y = 13
    print(x)

halo()      # 99
# print(y)    # error!

# =================================

# var local func merubah var global

x = 99
def halo():
    global x    # tanpa global, akan error!
    x = x + 5
    print(x)

halo()
print(x)