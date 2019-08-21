import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(1, figsize=(9, 3))

# plt.subplot(1 row, 3 col, position on 1)
# plt.subplot(1,3,1)
plt.subplot(131)
plt.bar(names, values)
plt.title('Plot 1')

plt.subplot(132)
plt.scatter(names, values)
plt.title('Plot 2')

plt.subplot(133)
plt.plot(names, values)
plt.title('Plot 3')

plt.suptitle('Categorical Plotting')
plt.show()