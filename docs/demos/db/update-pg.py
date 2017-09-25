import psycopg2

update_sql = "UPDATE test SET data = %s WHERE num = %s"
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
    # execute the UPDTE statement
    cur.execute(update_sql, ("ghjklm", 100))

    print("Rows modified:")
    print(cur.rowcount)

    # commit the changes to the database
    conn.commit()
    # close communication with the database
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
