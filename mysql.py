#!/usr/bin/python

import MySQLdb

value1 = raw_input("Enter First Value: ")
value2 = raw_input("Enter Second Value: ")
value1 = int(value1)
value2 = int(value2)

if value1 > value2:
    greater = value1
else:
    greater = value2

print "The greater of two no. is ", greater

# Open database connection
db = MySQLdb.connect("localhost", "amit", "amitt", "cpp")

# prepare a cursor object using cursor() method
cur = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO PROGRAM(Value1, Value2, Greater) \
           VALUES ('%d', '%d', '%d' )" % \
           (value1, value2, greater)
try:
    # Execute the SQL command
        cur.execute(sql)
    # Commit your changes in the database
        db.commit()
except:
    # Rollback in case there is any error
        db.rollback()

# disconnect from serve
db.close()
