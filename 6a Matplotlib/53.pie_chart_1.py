
import matplotlib.pyplot as plt

slice = [9, 3, 5, 7]
activity = ['Tidur', 'Tahajud', 'Subuh', 'Berangkat']
# cols = ['c', 'm', 'r', 'k']

# plt.pie(slice, labels=activity)
# plt.pie(slice, labels=activity, colors=cols)
# plt.pie(slice, labels=activity, startangle=90)
# plt.pie(slice, labels=activity, shadow=True)
# plt.pie(slice, labels=activity, counterclock=False)
# plt.pie(slice, labels=activity, explode=(0,0.2,0,0))  # explode=(data1, data2, data3, data4) 
# plt.pie(slice, labels=activity, autopct='%1.1f%%')
plt.pie(slice, labels=activity, autopct='%1.1f%%', textprops={'color':"r"})

# custom warna value & label:
# wedge, label, persen = plt.pie(slice, labels=activity, autopct='%1.1f%%', textprops={'color':"r"})
# for i in persen:
#     i.set_color('white')
# for i in wedge:
#     i.set_linewidth(1)
#     i.set_edgecolor('k')

plt.title('Tes Plotting Data\nby Lintang Wisesa')
plt.show()

# ========================

data = [72, 73, 35]
notes = ['RMA', 'BAR', 'DRAW']
wedge, label, persen = plt.pie(
    data, labels=notes, colors=['w', 'purple', 'lightblue'],
    autopct=lambda x: '{:.1f}%\n({})'.format(x, int(round(x * sum(data)/100)))
)
for i in wedge:
    i.set_linewidth(1)
    i.set_edgecolor('k')
for i in persen:
    i.set_color('w')
persen[0].set_color('k')
label[1].set_color('purple')

plt.show()