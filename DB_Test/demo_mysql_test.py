import mysql.connector

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="headfirst"
)

print(mydb)
