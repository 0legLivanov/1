import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 5 * np.pi)
y1 = np.cos(x1)

x2 = np.linspace(0, 5 * np.pi)
y2 = np.sin(x2)

x3 = np.linspace(0, 10)
y3 = x3**2

x4 = np.linspace(0.01, 10)
y4 = 2 / x4

plt.subplot(2, 1, 1)
plt.plot(x1, y1)
plt.title("cos")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(x2, y2)
plt.title("sin")
plt.grid(True)

plt.show()

plt.subplot(2, 2, 1)
plt.plot(x3, y3)
plt.title("x**2")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(x4, y4)
plt.title("2/x")
plt.grid(True)

plt.show()
