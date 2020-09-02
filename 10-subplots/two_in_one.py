"""code below is for plotting two axis in one figure"""
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('median_salary_data.csv')
age = data['Age']
all_dev = data['All_Devs']
python = data['Python']
javascript = data['JavaScript']

fig1, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex='all', sharey='col')

ax1.plot(age, all_dev, label='All Developers', color='#444444', linestyle='--', linewidth=2)
ax1.set_title('Median Salaries by Age')
ax1.set_ylabel('Median Salary')
ax1.legend(loc='upper left')

ax2.plot(age, python, label='Python')
ax2.plot(age, javascript, label='JavaScript')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary')
ax2.legend()

fig1.tight_layout()
fig1.savefig('two_in_one.png')

plt.show()
