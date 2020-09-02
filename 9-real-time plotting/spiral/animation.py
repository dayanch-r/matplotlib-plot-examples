import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  # plots from real time data file

"""

first clear the data.csv file. then run the animation.py right after you run the spiral.py

"""

plt.style.use('fivethirtyeight')


def animation(_):
    
    """
    function that plots animation, we can't arguments empty and use self because we are gonna use
    this function inside the class FuncAnimation

    """
    data = pd.read_csv('data.csv')
    x = data['x']
    y = data['y']

    plt.cla()  # each time clears the screen so that new screen won't be plotted over the old one
    plt.plot(x, y, c='#4CE468', linewidth=2, linestyle='-', marker=None)  # c=color

    plt.tight_layout()


anim = FuncAnimation(plt.gcf(), animation, interval=1)  # gcf()=get current figure
# every time runs the animation function
# interval is frame time interval of animation in milliseconds

plt.title('Hypnotizing Spiral')

plt.tight_layout()

plt.show()
