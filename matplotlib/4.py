import matplotlib.pyplot as plt
import random


def f(n):
    labels = [str(i) for i in range(1, n + 1)]
    values = [random.randint(20, 120) for i in range(n)]
    plt.pie(values, labels=labels)
    plt.show()


f(12)
