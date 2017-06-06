import sqlite3

#AccountInfo Table -----------------------------------------------------

#Checking if the account exists when logging in
def isValidAccountInfo(uN, hP):
    db = sqlite3.connect("data/main.db")
    c = db.cursor()
    cmd = "SELECT * FROM AccountInfo WHERE username = '%s' AND hashedPass = '%s';"%(uN, hP)
    sel = c.execute(cmd).fetchone()
    db.close()
    if sel == None:
        return False
    return True

#Obtaining the user ID
def getUserID(uN):
    db = sqlite3.connect("data/main.db")
    c = db.cursor()
    cmd = "SELECT * FROM AccountInfo WHERE username = '%s';"%(uN)
    sel = c.execute(cmd).fetchone()
    db.close()
    return sel[4]

#Registering the account information and type of account
def registerAccountInfo(uN, hP, type):
    db = sqlite3.connect("data/main.db")
    c = db.cursor()        
    addAT = "INSERT INTO AccountInfo(username,hashedPass,userType,classes) VALUES ('%s','%s','%s','');"%(uN,hP,type)
    c.execute(addAT)
    db.commit()
    db.close()

#Checking if the accounts exists when registering
def doesUserExist(uN):
    db = sqlite3.connect("data/main.db")
    c = db.cursor()
    cmd = "SELECT * FROM AccountInfo WHERE username = '%s';"%(uN)
    sel = c.execute(cmd).fetchone()
    db.close()
    if sel == None:
        return False
    else:
        return True 

#Obtaining the user type
def getUserType(userID):
    db = sqlite3.connect("data/main.db")
    c = db.cursor()
    cmd = "SELECT * FROM AccountInfo WHERE userID = '%s';"%(userID)
    sel = c.execute(cmd).fetchone()
    userType = sel[2]
    print userType
    db.close()
    return userType

#Obtaining the password of a user
def getPass(userID):
    db = sqlite3.connect("data/main.db")
    c = db.cursor()
    cmd = "SELECT * FROM AccountInfo WHERE userID = '%s';"%(userID)
    sel = c.execute(cmd).fetchone()
    password = sel[1]
    print password
    db.close()
    return password

#Channging the password of the user
def changePass(userID, newPass):
    db = sqlite3.connect("data/main.db")
    c = db.cursor()
    cmd = "UPDATE AccountInfo SET hashedPass = '%s'WHERE UserID = %d;"%(newPass, userID)
    c.execute(cmd)
    db.commit()
    db.close()

#Getting the array of the classes that the user has
def getClasses(userId):
    db = sqlite3.connect("data/main.db")
    c = db.cursor()
    cmd = "SELECT * FROM AccountInfo WHERE userID = '%s';"%(userId)
    sel = c.execute(cmd).fetchone()
    classes = sel[3].split("::")
    db.close()
    return classes[:-1] #removes the last empty string as a result of the delimiter
	
#Adding a new class to a user's schedule
def addClass(userId, classId):
    classes = getClasses(userId)
    classes += (str(classId) + "::")
    db = sqlite3.connect("data/main.db")
    c = db.cursor()
    cmd = "UPDATE AccountInfo SET classes = '%s' WHERE UserID = %d;"%(classes, userId)
    c.execute(cmd)
    db.commit()
    db.close()

#Events Table -----------------------------------------------------
#Registers event into the Events table
def createEvent(name,month,day,year,description):
	db = sqlite3.connect("data/main.db")
	c = db.cursor()
	c.execute("INSERT INTO Events(name,month,day,year,description) VALUES (?,?,?,?,?);",[name,month,day,year,description])
	db.commit()
	db.close()
	
def removeEvent(id):
	db = sqlite3.connect("data/main.db")
	c = db.cursor()
	c.execute("DELETE FROM Events WHERE id = ?",[id])
	db.commit()
	db.close()

#Grabs all information about the event
def getEvent(month,day,year):
	db = sqlite3.connect("data/main.db")
	c = db.cursor()
	cmd = "SELECT * FROM Events WHERE (month = '%s' AND day = '%d' AND year = '%d');"%(month,day,year)
	sel = c.execute(cmd).fetchone()
	if sel != None:
		return sel[1:]
	return sel

def getEvents():
	db = sqlite3.connect("data/main.db")
	c = db.cursor()
	cmd = "SELECT * FROM EVENTS"
	sel = c.execute(cmd).fetchall()
	print sel