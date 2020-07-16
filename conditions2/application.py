from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/<string:day>")
def day(day):
	day_today = datetime.datetime.today().strftime('%A')	# Take day of today
	answer = day_today == day 								# Compare with day to be checked

	if answer:
		answer = f"Yes, it is {day}"
	else:		
		answer = f"No, it is not {day}"						# Format the answer
	return render_template("check_day.html",answer=answer)	# Show the answer