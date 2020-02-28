import numpy as np

# =====================================================
# 0. all val dalam numpy array memiliki type yg sama (homogen) 

# =====================================================
# 1. numpy arrat dpt dibuat dr set, 
#    tp tetap sifat set = no index

a = np.array({1,2,3,4,5})
print(a)
# print(a[0]) # error!

# =====================================================
# 2. tidak boleh sisipkan str di beda numpy array int

a = np.array([1,2,3,4,5])
# a[0] = 'Andi' 
# print(a)  # akan error krn tdk bisa sisipkan str ke numpy int
a[0] = 12 
print(a)  # bisa krn sisipkan int ke numpy int

# =====================================================
# 3. int yg disisipkan ke numpy str akan berubah jd str,
#    dg panjang digit tidak lebih dr pjg karakter elemen terpjg

a = np.array(['a', 'b', 'c'])
a[0] = 120
print(a)  # ['1' 'b' 'c']

a = np.array(['andi', 'budi', 'caca'])
a[0] = 120
print(a)  # ['120' 'budi' 'caca']