# ESTABLISH A CONNECTION
import mysql.connector

connection = mysql.connector.connect(
    host='your_host',
    user='your_user',
    password='your_password',
    database='your_database'
)

# CHECK CONNECTION STATUS
if connection.is_connected():
    print("connection successfully :)")
else:
    print("connection error!")

# CREATE CURSOR
cursor = connection.cursor()

# SELECT QUERY
cursor.execute("show databases")

# INSERT QUERY
sql = "INSERT INTO table_name (id, name) VALUES (%s, %s)"
val = (101, "Maxim")
cursor.execute(sql, val)
connection.commit()

# UPDATE QUERY
sql = "UPDATE table_name SET id = '102' WHERE name = 'Maxim'"
cursor.execute(sql)
connection.commit()

# DELETE QUERY
sql = "DELETE FROM table_name WHERE name = 'Maxim'"
cursor.execute(sql)
connection.commit()

# FETCH ONE ROW
cursor.execute("SELECT * FROM table_name WHERE name = 'Maxim'")
data = cursor.fetchone()
print(data)

# FETCH ALL ROW
cursor.execute("SELECT * FROM table_name")
data = cursor.fetchall()
for i in data:
    print(i)

# COUNT ROWS
cursor.execute("SELECT COUNT(*) FROM table_name")
data = cursor.fetchone()
print("User :", data[0])

# %s FORMAT SPECIFIER
name = "Maxim"
sql = "SELECT * FROM table_name WHERE name = %s"
cursor.execute(sql, (name,))

# format() METHOD
name = "Maxim"
sql = "SELECT * FROM table_name WHERE name = '{}'".format(name)
cursor.execute(sql)

# CREATE DATABASE
cursor.execute("CREATE DATABASE test")
