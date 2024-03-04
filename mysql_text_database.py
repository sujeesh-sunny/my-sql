import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="sujeesh_usr", password="Mysql@121212", database="Relaince_Grocery_Store ")
cursor = mydb.cursor()

cursor.execute("CREATE TABLE example_table4 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

query = "INSERT INTO example_table4 (name, age) VALUES (%s, %s)"
values = [("John", 30),
          ("Alice", 24),
          ("Bob", 35),
          ("Eva", 28),
          ("Charlie", 40),
          ("Diana", 22),
          ("Frank", 45),
          ("Grace", 25),
          ("Henry", 38),
          ("Ivy", 23)]

cursor.executemany(query, values)

mydb.commit()

cursor.execute("SELECT * FROM example_table4")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
mydb.close()
