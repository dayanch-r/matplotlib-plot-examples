import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn-dark')

data = pd.read_csv('data.csv')

data['Date'] = pd.to_datetime(data['Date'])     # turns string values in data['Date'] to datetime type
data.sort_values('Date', inplace=True)          # sorts the data according to date.
                                                # inplace means: data['Date'] = data.sort_values('Date')

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='-', marker=None)  # marker assigns or removes markers

date_format = mpl_dates.DateFormatter('%b, %d %Y')  # we can create our own date format
plt.gca().xaxis.set_major_formatter(date_format)    # here we set the date format to the one that we created
                                                    # gca() = get current axis

plt.gcf().autofmt_xdate()   # rotates the dates a little bit so that it looks better and not crowded
                            # gcf() = get current figure

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Prices')

plt.grid(alpha=.6)
plt.tight_layout()

plt.savefig('plot_date.png')

plt.show()
