import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

# figure 1
plt.figure(1, figsize=(9, 3))

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

# ===========================================

# figure 2
plt.figure(2, figsize=(9, 3))

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
# plt.suptitle('Categorical Plotting', y=1.1, va='top', ha='left')

# =========================================

plt.show()