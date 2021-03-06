import matplotlib.pyplot as plt
import math
import numpy as np

t = np.arange(0, 5, 0.1)
y1 = np.sin(np.pi * t)
y2 = np.sin(np.pi * t + np.pi / 2)
y3 = np.sin(np.pi * t - np.pi / 2)

plt.plot(t, y1, t, y2, t, y3)
plt.show()
