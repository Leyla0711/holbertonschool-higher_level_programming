#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user, passwd=mysql_password, db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute a query to fetch all states, sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results and display them
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
