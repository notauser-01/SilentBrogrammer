from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False 
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

name = ""
posts = []

@app.route("/", methods=["GET", "POST"])
def flaskform():

	if request.method == "POST":
		name = request.form.get("name")

	return render_template("flaskform.html")

@app.route("/flaskform2", methods=["GET", "POST"])
def flaskform2():

	if request.method == "POST":
		post = request.form.get("post")
		posts.append(post)

	return render_template("flaskform2.html", posts=posts)