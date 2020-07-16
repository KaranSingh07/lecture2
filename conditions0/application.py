from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
	now = datetime.datetime.now()

	new_year = now.month==1 and now.date == 1

	if new_year:
		new_year = "YES it is!"
	else:
		new_year = "NO it is not."
	return render_template("index.html", new_year=new_year)
