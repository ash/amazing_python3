# Reading data from a CSV file

import csv

with open('288-data.csv') as data:
    reader = csv.DictReader(data)

    for row in reader:
        print('On ' + row['date'] + ':')

        ctr = round(100 * 
            int(row['clicks']) /
            int(row['displays']), 2
        ) # ignore 0/0

        print('CTR: ' + str(ctr) + '%\n')