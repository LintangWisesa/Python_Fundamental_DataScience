# https://sumberbelajar.belajar.kemdikbud.go.id/sumberbelajar/tampil/Sistem-Persamaan-Linear-dengan-Metode-Grafik-2008/konten3.html

import numpy as np
import matplotlib.pyplot as plt
# 3x + y = 15
# x + y = 7

# ====================================
# 3x + y = 15
# titik potong 1 dg sumbu-x => y = 0  => 3x = 15
# | 3 | | x | = | 15 |
x1 = np.linalg.solve([[3]], [15])[0]
y1 = 0
print(x1, y1)
# titik potong 2 dg sumbu-y => x = 0  => y = 15
# | 1 | | y | = | 15 |
y2 = np.linalg.solve([[1]], [15])[0]
x2 = 0
print(x2, y2)

# ====================================
# x + y = 7
# titik potong 1 dg sumbu-x => y = 0  => x = 7
# | 1 | | x | = | 7 |
x3 = np.linalg.solve([[1]], [7])[0]
y3 = 0
print(x3, y3)
# titik potong 2 dg sumbu-y => x = 0  => y = 7
# | 1 | | y | = | 7 |
y4 = np.linalg.solve([[1]], [7])[0]
x4 = 0
print(x4, y4)

# ====================================
# 3x + y = 15
# x + y = 7
# titik hasilnya
# | 3 1 | | x | = | 15 |
# | 1 1 | | y |   | 7 |
a = np.array([[3,1], [1,1]])
b = np.array([15,7])
hasil = np.linalg.solve(a, b)
print(hasil)

plt.plot([x1, y1], [x2, y2], 'b-', label='3x + y = 15', linewidth=2)
plt.plot([x3, y3], [x4, y4], 'g-', label='x + y = 7', linewidth=2)
plt.plot(hasil[0], hasil[1], 'yo', markersize=20)
plt.annotate('Titik\npotong\n(4,3)', xy=(hasil[0], hasil[1]), xytext=(5, 4),
    arrowprops=dict(facecolor='r', shrink=0.1),
)

plt.grid(True)
plt.legend()
plt.savefig('45.soal_draw_linerEq.png')
plt.show()