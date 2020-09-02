import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-notebook')


def animation(_):
    data = pd.read_csv('data.csv')

    x = data['x']
    y1 = data['y1']
    y2 = data['y2']

    plt.cla()
    plt.plot(x, y1, label='channel 1', color='green')
    plt.plot(x, y2, label='channel 2', color='orange')

    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.grid(alpha=.3)


ani = FuncAnimation(plt.gcf(), animation, interval=500)

plt.tight_layout()

plt.show()
