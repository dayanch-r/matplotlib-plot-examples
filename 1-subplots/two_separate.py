
"""code below is for plotting two axis in two separate figures"""

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('median_salary_data.csv')
age = data['Age']
all_dev = data['All_Devs']
python = data['Python']
javascript = data['JavaScript']

figure1, axis1 = plt.subplots()
figure2, axis2 = plt.subplots()

axis1.plot(age, all_dev, label='All Developers', color='#444444', linestyle='--', linewidth=2)
axis2.plot(age, python, label='Python')
axis2.plot(age, javascript, label='JavaScript')

axis1.set_title('Median Salaries by Age')
axis1.set_xlabel('Ages')
axis1.set_ylabel('Median Salary')

axis2.set_title('Median Salaries by Age')
axis2.set_xlabel('Ages')
axis2.set_ylabel('Median Salary')

plt.tight_layout()

figure1.savefig('figure1.png')
figure2.savefig('figure2.png')

plt.show()
