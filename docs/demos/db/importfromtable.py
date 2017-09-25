import psycopg2
import csv


with open('copytable.csv') as csvfile:

    conn = psycopg2.connect(
        dbname='spacedys',
        host='localhost',
        user='spacedys',
        password='password')

    # create a new cursor
    cur = conn.cursor()
    
    cur.copy_from(csvfile, 'test', columns=('num', 'data'), sep='\t')

#    for line in csvreader:
#        print(line)

    cur.close()
    conn.commit()    
    conn.close()
