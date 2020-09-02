from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('seaborn')

data = pd.read_csv('2019-05-1-data.csv')

views = data['views']
likes = data['likes']
ratio = data['ratio']

# c=color, cmap=color mapping style(you can choose), s=size(one can say sth like s=sizes,
#                                                           where sizes=list of sizes of each dot)
plt.scatter(views, likes, c=ratio, cmap='summer', marker='o', s=75, edgecolor='blue', linewidths=.5)

cbar = plt.colorbar()  # colorbar(): creates colorbar beside the scatter plot
cbar.set_label('like/dislike ratio')  # sets label to the colorbar

# plt.xscale('log'), plt.yscale('log')  # plots in logarithmic scale, try without it to see result

plt.title('Top 200 Trend Videos')
plt.xlabel('number ov views')
plt.ylabel('number of likes')
plt.grid(alpha=.75)

plt.tight_layout()

plt.savefig('scatter.png')

plt.show()
