from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", heading="Working")

@app.route("/<string:day>")
def check_day(day):
	today_day = datetime.datetime.today().strftime('%A')

	answer = today_day == day
	return render_template("check_day.html", answer=answer, user_day=day)

	# Conditions will be checked in HTML code.
