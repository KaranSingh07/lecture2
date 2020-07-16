from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
	return render_template("form.html")

@app.route("/hello", methods=["POST", "GET"])		
def hello():
	if request.method == "GET":
		return "Please submit the form instead."
	else:
		username = request.form.get("username")
		return render_template("hello.html", name=username)

	# This will only accept post request, this means going to the URL directly instead of submit button, it'll throw an error.
	# To accept those requests, add "get" to the methods.  