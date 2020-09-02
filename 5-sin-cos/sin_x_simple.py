import matplotlib.pyplot as plt
from numpy import arange, sin, pi

x = arange(0, 2*pi, 0.1)  # range of x values

sin_x = [sin(x) for x in x]
plt.plot(x, sin_x, label='sin(x)')

plt.title('A Beautiful Graph')
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend()  # legend(): shows labels

plt.grid(alpha=.25)
plt.show()  # shows graph
