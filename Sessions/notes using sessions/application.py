from flask import Flask, render_template, request, session
from flask_session import Session 

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"	# Storage at server side
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
	if session.get("notes") is None:
		session["notes"] = []
		# To check whether the notes are empty of not, if empty then initialize with empty list

	if request.method == "POST":
		note = request.form.get('note')
		if note:
			session["notes"].append(note)
		else:
			return "Note can'be empty."
		
	return render_template("index.html", notes=session["notes"])