# Kabir wants to write a program in python to insert the following record in the
# table named student in mysql database
# roll_no(Roll number) - integer
# name(Name) - string
# dob (Date of birth) – Date
# Fee – float

# Note the following to establish connectivity between python and mysql
# Host - localhost
# Username - root
# Password - tiger
# Database - School

# The values of fields roll_no, name, dob and fee has to be accepted from the user.
# Help Kabir to write the program in python

# import
import mysql.connector

# connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='database#90157324',
    database='school',
    auth_plugin="mysql_native_password"
)

# cursor
cursor = mydb.cursor()

# query
cursor.execute("CREATE DATABASE IF NOT EXISTS school")
mydb.commit()
cursor.execute("USE school")
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS student (
        roll_no INT PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        dob DATE,
        fee FLOAT
    );
    '''
)
mydb.commit()

# input
roll_no = int(input("Enter roll number : "))
name = input("Enter name : ")
dob = input("Enter dob (yyyy-mm-dd) : ")
fee = float(input("Enter fee : "))

# insert
sql = "INSERT INTO student (roll_no, name, dob, fee) VALUES (%s, %s, %s, %s)"
val = (roll_no, name, dob, fee)
cursor.execute(sql, val)

# commit
mydb.commit()

print("record inserted")

mydb.close()