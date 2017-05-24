#Initializes database

import sqlite3

db = sqlite3.connect("../data/main.db")
c = db.cursor()

accounts = "CREATE TABLE AccountInfo(username TEXT, hashedPass TEXT, userType TEXT, classes TEXT, userID INTEGER AUTOINCREMENT);"

classes = "CREATE TABLE Classes(id INTEGER, event TEXT);"

events = "CREATE TABLE Events(id INTEGER, name TEXT, date TEXT, description TEXT);"

c.execute(accounts)
c.execute(classes)
c.execute(events)

db.commit()
db.close()
