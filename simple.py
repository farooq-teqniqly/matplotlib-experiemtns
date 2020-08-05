import matplotlib.pyplot as plt

plt.axis([-15, 15, 0, 110])
plt.title("Quadratic Equation")
plt.plot(range(-10, 11), [x * x + 3 for x in range(-10, 11)])
plt.show()
