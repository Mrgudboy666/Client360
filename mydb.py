# Install Mysql on computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python
# https://codemy.com/git - for git help



import mysql.connector

# Connect to the database
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Mysql123#',
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS client360_db")

print("All done!")