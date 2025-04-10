import mysql.connector as conn

# myDB = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "123456789"
# )

# print(myDB)


cursor = conn.cursor()
cursor.execute("SELECT * FROM newdb.student")
for row in cursor:
    print(row)
    
conn.close()