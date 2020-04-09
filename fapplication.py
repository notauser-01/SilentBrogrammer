import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	now = datetime.datetime.now()
	smoke = (now.hour == 4 or now.hour == 16) and now.minute == 20
	smoke = True
	return render_template("home.html", smoke=smoke)
