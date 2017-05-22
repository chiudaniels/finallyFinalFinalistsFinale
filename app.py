from flask import Flask, render_template, request, session, url_for, redirect

from utils import tools

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
		tools.register(data["username"], data["p1"])
		session["userID"] = tools.getUserID(data["username"])
	return redirect(url_for("showMainPage"))

#Helper Functions
def isLoggedIn():
	return "userID" in session

def getUserID():
	return session["userID"]

#running flask app
if __name__ == "__main__":
	app.debug = True
	app.run()
