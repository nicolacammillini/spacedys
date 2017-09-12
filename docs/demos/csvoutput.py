import csv

csvfile = open('csvoutput.csv', 'w')

csvwriter = csv.writer(csvfile, delimiter=',')
csvwriter.writerow(['campo1', 'campo2', 'campo3'])
csvwriter.writerow(['valore1', 'valore2', 'valore3'])
csvfile.close()
    

