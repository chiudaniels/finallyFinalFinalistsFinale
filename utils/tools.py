import hashlib, sqlite3
import database

#Account Management---------------------------------------------------------
#given login information, check database
def isValidLogin(userName, password):
    return database.isValidAccountInfo(userName, hashed(password))

#Verify if password change is valid
def verify(userID, oldPass, pass1, pass2):
    return hashed(oldPass) == database.getPass(userID) and pass1 == pass2

#Change the current password
def changePass(userID, password):
    return database.changePass(userID, hashed(password))

#Obtaining the user ID
def getUserID(username):
    return database.getUserID(username)

#Obtaining the user type
def getUserType(userID):
    return database.getUserType(userID)
    
#Check if the account exists in the database
def isValidRegister(pass1, pass2, username):
    return pass1 == pass2 and (not database.doesUserExist(username))

#Register the User
def register(username, password,type):
    return database.registerAccountInfo(username, hashed(password),type)

#Events----------------------------------------------------
#Get an event based on date
def getEvent(day,month,year):
	return database.getEvent(day,month,year)

#Get the event's information
def getEventInfo(eventID):
	return database.getEventInfo(eventID)

#HELPERS--------------------------------------
def hashed(unhashed):
    return hashlib.sha512(unhashed).hexdigest()
