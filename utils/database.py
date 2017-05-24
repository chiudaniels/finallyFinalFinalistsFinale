import sqlite3

#AccountInfo Table -----------------------------------------------------
def isValidAccountInfo(uN, hP):
    db = sqlite3.connect("data/main.db")
    c = db.cursor()
    cmd = "SELECT * FROM AccountInfo WHERE username = '%s' AND hashedPass = '%s';"%(uN, hP)
    sel = c.execute(cmd).fetchone()
    db.close()
    if sel == None:
        return False
    return True

def getUserID(uN):
    db = sqlite3.connect("data/main.db")
    c = db.cursor()
    cmd = "SELECT * FROM AccountInfo WHERE username = '%s';"%(uN)
    sel = c.execute(cmd).fetchone()
    db.close()
    return sel[4]

def registerAccountInfo(uN, hP, type):
    db = sqlite3.connect("data/main.db")
    c = db.cursor()
        
    addAT = "INSERT INTO AccountInfo(username,hashedPass,userType,classes) VALUES ('%s','%s','%s','');"%(uN,hP,type)
    c.execute(addAT)
    db.commit()
    db.close()

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

def getUserType(userID):
    db = sqlite3.connect("data/main.db")
    c = db.cursor()
    cmd = "SELECT * FROM AccountInfo WHERE userID = '%s';"%(userID)
    sel = c.execute(cmd).fetchone()
    userType = sel[2]
    print userType
    db.close()
    return userType

def getPass(userID):
    db = sqlite3.connect("data/main.db")
    c = db.cursor()
    cmd = "SELECT * FROM AccountInfo WHERE userID = '%s';"%(userID)
    sel = c.execute(cmd).fetchone()
    password = sel[1]
    print password
    db.close()
    return password

def changePass(userID, newPass):
    db = sqlite3.connect("data/main.db")
    c = db.cursor()
    cmd = "UPDATE AccountInfo SET hashedPass = '%s'WHERE UserID = %d;"%(newPass, userID)
    c.execute(cmd)
    db.commit()
    db.close()
