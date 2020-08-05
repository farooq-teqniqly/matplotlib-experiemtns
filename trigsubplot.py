import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 5, 0.1)

y1 = np.sin(2 * np.pi * t)
y2 = np.cos(2 * np.pi * t)
y3 = t * t + 5
y4 = t * t * t


plt.subplot(221)
plt.title(r"$y = sin(2\pi t)$")
plt.xlabel("x")
plt.ylabel("y")

for i in t:
    if i % 2 == 0:
        plt.text(i, 0, i, fontsize=6, color="red", bbox={"facecolor": "yellow", "alpha": 0.5})

plt.plot(t, y1)

plt.subplot(222)
plt.title(r"$y=t^2 + 5$")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(t, y3, "y")

plt.subplot(223)
plt.title(r"$y=cos(2\pi t)$")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(t, y2, "r")

plt.subplot(224)
plt.title(r"$t^3$")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(t, y4, "g")
plt.legend([r"Value of y"])

plt.show()
