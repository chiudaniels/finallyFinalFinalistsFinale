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
#Create an event
def createEvent(name,month,day,year,description):
	return database.createEvent(name,month,day,year,description)

#Remove an event
def removeEvent(id):
	return database.removeEvent(id)
	
#Get an event based on date
def getEvent(month,day,year):
	return database.getEvent(month,day,year)

#Get a list of all events
def getEvents():
	return database.getEvents()

#Get the event's information
def getEventInfo(eventID):
	return database.getEventInfo(eventID)

#Classes----------------------------------------------------
#Add a class to an account
def addClass(userID, classID):
	return database.addClass(userID,classID)

def getClasses(userID):
	return database.getClasses(userID)
	
#HELPERS--------------------------------------
def hashed(unhashed):
    return hashlib.sha512(unhashed).hexdigest()
