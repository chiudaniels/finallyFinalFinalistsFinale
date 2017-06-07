from flask import Flask, render_template, request, session, url_for, redirect

from utils import tools

import json

app = Flask(__name__)
app.secret_key = "narutoisbased"

@app.route('/')
def showMainPage():
    if (not isLoggedIn()):
        return render_template('main.html', isLoggedIn = str(False))
    else:
        return render_template('main.html', isLoggedIn = str(True))

@app.route('/logout/')
def logout():
	if isLoggedIn():
		session.pop('userID')
	return redirect(url_for("showMainPage"))

@app.route('/login/', methods = ['POST'])
def login():
	data = request.form
	if tools.isValidLogin(data['username'], data['pass']):
		session['userID'] = tools.getUserID(data['username'])
	return redirect(url_for("showMainPage"))

@app.route("/register/", methods = ['POST'])
def register():
	data = request.form
	if tools.isValidRegister(data["p1"], data["p2"], data["username"]):
		if data["code"] == "8Y4vnAUlW8X0RQkc146p":
			tools.register(data["username"], data["p1"],"teacher")
		else:
			tools.register(data["username"], data["p1"],"teacher")
		session["userID"] = tools.getUserID(data["username"])
	return redirect(url_for("showMainPage"))

@app.route("/addEvent/")
def addEvent():
	if isLoggedIn():
		if tools.getUserType(session["userID"]) == "teacher":
			return render_template("form.html", isLoggedIn = str(True))
	else:	
		return redirect(url_for("showMainPage"))

@app.route("/eventList/")
def eventList():
	return render_template("eventList.html")

@app.route("/pushEvent/", methods = ['POST'])
def pushEvent():
	data = request.form
	tools.createEvent(data["title"],data["month"],int(data["day"]),int(data["year"]),data["description"])
	return redirect(url_for("showMainPage"))

@app.route("/eventExists/")
def eventExists():
	data = request.args

	month = data.get("month")
	day = data.get("day")
	year = data.get("year")

	event = tools.getEvent(month,int(day),int(year))
	if event != None:
		event = {"id" : event[0], "title" : event[1], "month" : event[2], "day" : event[3], "year" : event[4], "description" : event[5]}
	
	return json.dumps(event)

@app.route("/eventRemoval/")
def eventRemoval():
	data = request.args
	id = data.get("id")
	if isLoggedIn():
		print "moo"
		if tools.getUserType(session["userID"]) == "teacher":
				tools.removeEvent(int(id))
				return json.dumps({"type" : "teacher"})
	else:	
		return json.dumps({"type" : "student"})

#Helper Functions
def isLoggedIn():
	return "userID" in session

def getUserID():
	return session["userID"]

#running flask app
if __name__ == "__main__":
	app.debug = True
	app.run()
