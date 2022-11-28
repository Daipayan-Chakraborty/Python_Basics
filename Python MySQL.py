
# Connecting python to MySQL Database

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="24535571",
    database="python_sql"
)
print(mydb)
c = mydb.cursor()

# To show the existing databases
c.execute("show databases")
for i in c:
    print(i)

# Creating a database
c.execute("CREATE DATABASE python_sql")

# Creating a Table in python_sql
c.execute("CREATE TABLE school (id INT(5), name VARCHAR(255), address VARCHAR(255))")

# Inserting multiple records into school table
sql = 'INSERT INTO school (id, name, address) VALUES ("01","John","Chennai"),("02","Tom","Mumbai"),("03","Harry",' \
      '"Delhi"),("04", "Ben", "Assam")'
c.execute(sql)
mydb.commit()

# Reading the complete data from the TABLE school
c.execute("SELECT * FROM school")
result = c.fetchall()

for x in result:
    print(x)

# Filtering using WHERE clause
sql = "SELECT * FROM school WHERE address ='chennai'"
c.execute(sql)
result = c.fetchall()

for x in result:
    print(x)

# Creating a second Table in python_sql food
# Inserting multiple records into school table
c.execute("CREATE TABLE food (id INT(5), name VARCHAR(255), items VARCHAR(255))")
sql = 'INSERT INTO food (id, name, items) VALUES ("01","John","Pizza"),("02","Tom","Burger"),("03","Harry",' \
      '"Icecream"),("04", "Ben", "Fresh Juice")'
c.execute(sql)
mydb.commit()

# Reading the complete data from the TABLE food
c.execute("SELECT * FROM food")
result = c.fetchall()

for x in result:
    print(x)

# JOINS
# To join both the table food & school using inner join
sql = " SELECT s.name,address,items FROM school as s \
      INNER JOIN food as f \
      ON s.id = f.id"
c.execute(sql)
result = c.fetchall()

for x in result:
    print(x)

