import csv, time
from math import cos, sin

theta, r, x, y = 0, 0, 0, 0

fieldnames = ['theta', 'r', 'x', 'y']  # r, theta = polar coordinates
                                       # x, y = cartesian coordinates

with open('data.csv', 'w') as csv_file:  # creates or opens csv file
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)  # assigns header for datafile
    csv_writer.writeheader()

while 1:  # incessantly continues
    with open('data.csv', 'a') as csv_file:  # opens csv file in appending mode
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {'theta': theta, 'r': r, 'x': x, 'y': y}

        csv_writer.writerow(info)
        print(info['theta'], info['r'], info['x'], info['y'])

        theta += 0.01
        r = theta
        x, y = r * cos(theta), r * sin(theta)
    time.sleep(.01)
