import random, csv, time

x = 0
y1 = 1000
y2 = 1000

fieldnames = ['x', 'y1', 'y2']

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while 1:
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {'x': x, 'y1': y1, 'y2': y2}

        csv_writer.writerow(info)
        print(x, y1, y2)

        x += 1
        y1 += random.randint(-5, 7)
        y2 += random.randint(-5, 6)

        time.sleep(.5)
