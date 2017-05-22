from flask import Flask, render_template, request, session, url_for, redirect

from utils import tools

app = Flask(__name__)
app.secret_key = "narutoisbased"

@app.route('/')
def showMainPage():
    return render_template("main.html")

@app.route('/logout/')
def logout():
	if isLoggedIn():
		session.pop('userID')
	return redirect(url_for("root"))

@app.route('/login/', methods = ['POST'])
def login():
	data = request.form
	if utils.isValidLogin(data['username'], data['pass']):
		session['userID'] = utils.getUserID(data['username'])

@app.route("/register")
def register():
	data = request.form
	if utils.isValidRegister(data["p1"], data["p2"], d["username"]):
		utils.register(data["username"], data["p1"])
		session["userID"] = utils.getUserID(data["username"])
	return redirect(url_for("root"))

#Helper Functions
def isLoggedIn():
	return "userID" in session

def getUserID():
	return session["userID"]

#running flask app
if __name__ == "__main__":
	app.debug = True
	app.run()
