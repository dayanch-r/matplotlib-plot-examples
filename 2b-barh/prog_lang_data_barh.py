import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use('fivethirtyeight')

data = pd.read_csv('prog_lang_data.csv')
language_responses = data['LanguagesWorkedWith']

lang_counter = Counter()

for response in language_responses:
    lang_counter.update(response.split(';'))

languages, popularity = map(list, zip(*lang_counter.most_common(15)))
languages.reverse(), popularity.reverse()

plt.barh(languages, popularity, color='#444444', label='languages')

plt.title('most popular programming languages'.title())
plt.xlabel('# of responses')
plt.tight_layout()
plt.savefig('prog_lang_data_barh.png')

plt.show()
