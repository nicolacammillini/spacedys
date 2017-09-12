import csv

csvfile = open('csvoutput.csv')

csvreader = csv.reader(csvfile)

# csv.reader supports iterator protocol
for line in csvreader:
    print(','.join(line))

