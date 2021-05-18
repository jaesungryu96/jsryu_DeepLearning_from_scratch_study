import matplotlib.pyplot as plt


plt.plot([1, 0], [0, 1], 'bo')
plt.plot([0, 1], [0, 1], 'rv')
plt.axis([-0.1, 1.5, -0.1, 1.5])
plt.xlabel('x1')
plt.ylabel('x2')

plt.show()
