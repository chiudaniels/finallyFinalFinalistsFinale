#Initializes database

import sqlite3

db = sqlite3.connect("../data/main.db")
c = db.cursor()

accounts = "CREATE TABLE AccountInfo(username TEXT, hashedPass TEXT, userType TEXT, classes TEXT, userID INTEGER PRIMARY KEY AUTOINCREMENT);"

classes = "CREATE TABLE Classes(id INTEGER PRIMARY KEY AUTOINCREMENT, event TEXT);"

events = "CREATE TABLE Events(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, date TEXT, description TEXT);"

c.execute(accounts)
c.execute(classes)
c.execute(events)

db.commit()
db.close()
