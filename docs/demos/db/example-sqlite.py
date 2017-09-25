import sqlite3

# Connect to an existing database
connection = sqlite3.connect("exampledb")

# Open a cursor to perform database operations
cursor = connection.cursor()

# Execute a command: this creates a new table
cursor.execute("CREATE TABLE test (id integer primary key, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cursor.execute("INSERT INTO test (num, data) VALUES (?, ?)", (100, "abc'def"))


# Query the database and obtain data as Python objects
cursor.execute("SELECT * FROM test;")
results = cursor.fetchone()
print(results)


# Make the changes to the database persistent
connection.commit()

# Close communication with the database
cursor.close()
connection.close()
