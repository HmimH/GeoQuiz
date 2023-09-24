from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///haahelmi"
db = SQLAlchemy(app)
loggedin = False

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/highscores")
def scores():
    return "Highscores!"
    
@app.route("/newgame")
def newgame():
    return "start a new game here"
    
@app.route("/loginuser")
def loginuser():
    return render_template("username.html")

@app.route("/password", methods=['POST'])
def loginpassword():
    if loggedin == True:
        return render_template("/alreadyin.html")
    
    username = request.form["name"]
    
    getusercolumn = db.session.execute("SELECT username FROM users")
    userlist = getusercolumn.fetchall()
    if username in userlist:
        return render_template("passworduser.html", username = username)
    return render_template("passwordnewuser.html")

