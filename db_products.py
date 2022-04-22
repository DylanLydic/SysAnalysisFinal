import sqlite3 as sql 

conn = sql.connect("database.db")
conn.execute("CREATE TABLE Inventory (product TEXT, description TEXT, quantity INTEGER, checkin TEXT)")
conn.close()
print("Table Created")