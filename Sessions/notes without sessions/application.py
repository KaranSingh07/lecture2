from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		note = request.form.get('note')
		notes.append(note)
		
	return render_template("index.html", notes=notes)


# Here every note will be shown up to every user. That's not we want. Go to the "notes using sessions"
# to see the magic of Sessions.