import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(-1, 1.5, 0.1)
x2 = -1 * x1 + 1.5

plt.plot([1], [1], 'bo')
plt.plot([0, 1, 0], [0, 0, 1], 'rv')
plt.plot(x1, x2)
plt.fill_between(x1[:], x2[:], alpha=0.1)
plt.axis([-0.1, 1.5, -0.1, 1.5])
plt.xlabel('x1')
plt.ylabel('x2')

plt.show()
