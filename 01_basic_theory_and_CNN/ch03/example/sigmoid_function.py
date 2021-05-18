import numpy as np
import matplotlib.pyplot as plt
from step_function import step_function


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

"""
x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(x)
y2 = step_function(x)
plt.plot(x, y1)
plt.plot(x, y2, linestyle='--')
plt.ylim(-0.1, 1.1)
plt.show()
"""
