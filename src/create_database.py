# inital script which is required to create the database

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin"
)

mycursor = mydb.cursor()

try:
  mycursor.execute("CREATE DATABASE information")
except Exception as e:
    print("Program failed due to following error")
    print(e)