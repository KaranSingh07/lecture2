from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		if session["notes"] is None:
			session["notes"] = []

		note = request.form['note']
		if note:
			session["notes"].append(note)
		else:
			return render_template("index.html", notes=session["notes"], msg1_text="Note should not be empty!")

	return render_template("index.html", notes=session["notes"])

@app.route("/remove", methods=["GET", "POST"])
def remove():
	if request.method == "POST":
		index = int(request.form['index'])
		if index <= len(session["notes"]) and index>=0:
			del session["notes"][index-1]
		else:
			return render_template("index.html", notes=session["notes"], msg2_text="Invalid index!")

		return render_template("index.html", notes=session["notes"])
	else:
		return "Submit the form instead!"