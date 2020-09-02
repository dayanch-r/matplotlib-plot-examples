from matplotlib import pyplot as plt
import pandas as pd

# plt.xkcd()
# plt.style.available
plt.style.use('fast')

data = pd.read_csv('median_salary_data.csv')

ages_x = data['Age']
dev_salaries = data['All_Devs']
py_dev_salaries = data['Python']
js_dev_salaries = data['JavaScript']
overall_median = 57287


# plt.plot(ages_x, js_dev_salaries, label='JavaScript')
plt.plot(ages_x, py_dev_salaries, label='Python', linewidth='2')
plt.plot(ages_x, dev_salaries, label='All Devs', color='#444444', linestyle='--', linewidth='2')

# plt.fill_between(ages_x, py_dev_salaries, overall_median, alpha=.25)
plt.fill_between(ages_x, py_dev_salaries, dev_salaries, label='Above avg',
                 where=(py_dev_salaries > dev_salaries), interpolate=True, alpha=.25)  # interpolate fills out evenly

plt.fill_between(ages_x, py_dev_salaries, dev_salaries, label='Below avg', color='red',
                 where=(py_dev_salaries <= dev_salaries), interpolate=True, alpha=.25)

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.legend()  # shows labels
plt.grid(alpha=.25)  # alpha fades out sharpness of grid lines
plt.tight_layout()  # adds automatic padding to the plot to make it look better
plt.savefig('median_salary.png')  # saves the plot to current directory

plt.show()  # if you don't type this graph wont be shown
