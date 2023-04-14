import mysql.connector
dbconfig = {'host': '127.0.0.1', 'user': 'root',
            'password': 'headfirst', 'database': 'vsearchlogDB', }


#! Don't forget to make sure the SQL server is powered on with sudo service mysql start
conn = mysql.connector.connect(**dbconfig)

cursor = conn.cursor()

_SQL = """show tables"""
cursor.execute(_SQL)

res = cursor.fetchall()
