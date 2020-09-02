from matplotlib import pyplot as plt

"""pie charts are good with fewer amount of slice elemnts. Otherwise, chart will be overcrowded. 
    Bar or barh would be good with many data elements"""

plt.style.use('fast')

slices = [26515, 26484, 86514, 92554, 65488]
labels = ['javascript', 'html/css', 'sql', 'python', 'java']
colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f', '#e79d7d']
explode = [0, 0, 0, .05, 0]  # moves the 4th slice element away from center with length of (.05 * radius)

plt.pie(slices, labels=labels, colors=colors, explode=explode, wedgeprops={'edgecolor': '#000000'},  # #000000=black
        shadow=True, startangle=150, autopct='%1.1f%%')  # startangle rotates, autopct shows percentage

plt.title('pie chart'.title())
plt.tight_layout()
plt.savefig('prog_lang_pie.png')

plt.show()
