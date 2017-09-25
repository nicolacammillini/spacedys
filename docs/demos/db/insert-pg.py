import psycopg2

insert_sql = "INSERT INTO test (num, data) VALUES (%s, %s)"
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
    # execute the INSERT statement
    cur.execute(insert_sql, (100, "abcdef"))
    # commit the changes to the database
    conn.commit()
    # close communication with the database
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()