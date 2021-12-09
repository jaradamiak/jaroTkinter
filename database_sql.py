import mysql.connector

#SET MYSQL CONNECTION
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "password123",
	database = "testdb",
	)

#CREATE CURSOR INSTANCE
cur = mydb.cursor()

#CREATE DATABASE
cur.execute("CREATE DATABASE testdb")

#SHOW DATABASE
cur.execute("SHOW DATABASES")

#CREATE TABLE
cur.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
cur.execute("SHOW TABLES")

#INSERT ONE RECORD
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
record1 = ("John", "john@codemy.com", 40)
cur.execute(sqlStuff, record1)
mydb.commit()

#INSERT MULTIPLE RECORDS
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
records = [("Tim", "tim@tim.com", 32),
	("Mary", "Mary@mary.com", 21),
	("Steve", "steve@steveEmail.com", 57),
	("Tina", "tina@somethingellse.com", 29),]
cur.executemany(sqlStuff, records)
mydb.commit()

#PULL DATA FROM THE TABLE
cur.execute("SELECT * FROM users")
result = cur.fetchall()
print("NAME\tEMAIL\t\t\tAGE\tID")
print("----\t-----\t\t\t---\t---")
for row in result:
	print(row[0] + "\t%s" %row[1] + "\t\t%s" %row[2] + "\t%s" %row[3])

#WHERE CLAUSE
cur.execute("SELECT * FROM users WHERE name =  'John'")
result = cur.fetchall()
for row in result:
	print(row)

#WHERE and LIKE WILDCARDS
cur.execute("SELECT * FROM users WHERE name LIKE '%i%'")
result = cur.fetchall()
for row in result:
	print(row)

# AND / OR Clause
cur.execute("SELECT * FROM users WHERE name LIKE '%i%' AND age = 29 AND user_id = 5")
result = cur.fetchall()
for row in result:
	print(row)

#UPDATING RECORDS
my_sql = "UPDATE users SET name = 'Johnny' WHERE user_id = 6"
cur.execute(my_sql)
mydb.commit()

#LIMIT RESULTS
cur.execute("SELECT * FROM users LIMIT 3 OFFSET 1")
result = cur.fetchall()
for row in result:
	print(row)

#ORDERING RESULTS
cur.execute("SELECT * FROM users ORDER BY age DESC")
result = cur.fetchall()
for row in result:
	print(row)

#DELETE RECORDS
my_sql = "DELETE FROM users WHERE name  = 'John'"
cur.execute(my_sql)
mydb.commit()

# DELETE DROP TABLE
my_sql = "DROP TABLE IF EXISTS users"
cur.execute(my_sql)