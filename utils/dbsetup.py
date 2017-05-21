#Initializes database

import sqlite3

db = sqlite3.connect("../data/main.db")
c = db.cursor()

accounts = "CREATE TABLE AccountInfo(username TEXT, hashedPass TEXT, userID INTEGER);"
c.execute(accounts)

db.commit()
db.close()
