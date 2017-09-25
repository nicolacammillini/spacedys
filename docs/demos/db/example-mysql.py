import mysql.connector

# Connect to an existing database
connection = mysql.connector.connect(
    database='spacedys', 
    host='localhost', 
    user='spacedys', 
    password='password')

# Open a cursor to perform database operations
cursor = connection.cursor()

# Execute a command: this creates a new table
cursor.execute("CREATE TABLE test (id INT AUTO_INCREMENT PRIMARY KEY, num INT, data VARCHAR(20));")

# Pass data to fill a query placeholders and let the driver perform
# the correct conversion (no more SQL injections!)
cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))


# Query the database and obtain data as Python objects
cursor.execute("SELECT * FROM test;")
results = cursor.fetchone()
print(results)


# Make the changes to the database persistent
connection.commit()

# Close communication with the database
cursor.close()
connection.close()
