import matplotlib.pyplot as plt
import numpy as np


def f(a, b):
    x1 = np.linspace(0, 30)
    s = a.split('+')
    s1 = b.split('+')
    y1 = int(a[0]) * x1 + int(s[1])
    x2 = np.linspace(0, 30)
    y2 = int(b[0]) * x2 + int(s1[1])
    plt.title("y = " + a + "       " + "y = " + b)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.show()


f("2x+30", "3x+20")
