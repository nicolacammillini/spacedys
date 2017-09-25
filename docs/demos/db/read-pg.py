import psycopg2

read_sql = "SELECT num, data FROM test"
conn = None
try:
    # connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname='spacedys',
        host='localhost',
        user='spacedys',
        password='password')
    # create a new cursor
    cur = conn.cursor()
    # execute the SELECT statement
    cur.execute(read_sql)
    
    results = cur.fetchmany(10)

    for result in results:
        print(result)

    # commit the changes to the database
    conn.commit()
    # close communication with the database
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()