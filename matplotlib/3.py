import matplotlib.pyplot as plt
import random


def f():
    plt.rcdefaults()
    fig, ax = plt.subplots()
    people = ('1', '2', '3', '4', '5', '6', '7')
    y_pos = [0, 1, 2, 3, 4, 5, 6]
    performance = [random.randint(0, 120), random.randint(0, 120), random.randint(0, 120), random.randint(0, 120),
                   random.randint(0, 120), random.randint(0, 120), random.randint(0, 120)]
    ax.barh(y_pos, performance, align='center', color='black', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.invert_yaxis()
    plt.show()


f()
