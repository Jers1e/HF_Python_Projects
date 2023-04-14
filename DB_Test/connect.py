import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="headfirst",
    database="vsearchlogDB"
)
