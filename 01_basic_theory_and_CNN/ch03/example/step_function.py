import numpy as np
import matplotlib.pyplot as plt


def step_function(x):
    y = x > 0
    return y.astype(np.int)

"""
x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
"""


#def step_function_0(x):
#    if x > 0:
#        return 1
#    else:
#        return 0