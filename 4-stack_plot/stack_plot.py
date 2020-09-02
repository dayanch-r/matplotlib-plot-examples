from matplotlib import pyplot as plt

"""we will plot working time progress of developers over days"""
plt.style.use('fast')

days = [i for i in range(1, 10)]

dev1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
dev2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
dev3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['developer1', 'developer2', 'developer3']
colors = ['#1B58FF', '#25E314', '#E3A733']  # you can specify your own colors

plt.stackplot(days, dev1, dev2, dev3, labels=labels, colors=colors)

plt.legend(loc=(.07, .05))  # coordinates given to locate the legend
plt.xlabel('Days'), plt.ylabel('Hours')
plt.title('my stack plot'.title())
plt.tight_layout()

plt.savefig('stack_plot.png')

plt.show()
