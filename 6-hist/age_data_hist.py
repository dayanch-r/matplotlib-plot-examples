from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
data = pd.read_csv('age_data.csv')

ages = data['Age']
median_age = 29
bins = [i for i in range(0, 110, 10)]

plt.hist(ages, bins=bins, edgecolor='black', log=True, alpha=.7)  # log = plot in logarithmic scale
plt.axvline(median_age, label='median age', color='red', linewidth='2', alpha=.5)  # axvline = axis vertical line

plt.title('A Beautiful Histogram')
plt.xlabel('Ages')
plt.ylabel('Number of Responses')

plt.legend()
plt.tight_layout()
plt.savefig('age_data_hist.png')

plt.show()
