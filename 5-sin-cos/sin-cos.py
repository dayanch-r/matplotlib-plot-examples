import matplotlib.pyplot as plt
from numpy import arange, sin, cos, pi

plt.style.use('seaborn-whitegrid')

figure, (axis_1, axis_2, axis_3) = plt.subplots(nrows=3, ncols=1, sharex='row')

x = arange(0, 2*pi, 0.1)  # range of x values
sin_x = [sin(x) for x in x]
cos_x = [cos(x) for x in x]

axis_1.plot(x, sin_x, label='sin(x)')
axis_1.set_ylabel('sin(x)')
axis_1.set_title('A Beautiful Graph')


axis_2.plot(x, cos_x, label='cos(x)', color='#FF871E')
axis_2.set_ylabel('cos(x)')

axis_3.plot(x, sin_x)
axis_3.plot(x, cos_x)

axis_3.fill_between(x, sin_x, alpha=.25)  # alpha: fades the colors
axis_3.fill_between(x, cos_x,  alpha=.25)

axis_3.set_xlabel('x values')
axis_3.set_ylabel('y values')


axis_1.axhline(y=0, color='black', linewidth='.5')  # axhline: axis horizontal line
axis_2.axhline(y=0, color='black', linewidth='.5')  # axhline: axis horizontal line
axis_3.axhline(y=0, color='black', linewidth='.5')  # axhline: axis horizontal line

figure.legend(loc=(.8, .91))  # legend(): shows labels

figure.tight_layout()  # helps to plot in nicer way
figure.savefig('sin-cos')  # saves the graph to the current directory as .png file

plt.show()  # shows graph
