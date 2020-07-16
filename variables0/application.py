from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	headline = "Hello there!"
	return render_template("index.html", headline=headline)

@app.route("/paragraph")
def paragraph():
	headline = "This is my webpage headline."
	paragraph = "This is the description paragraph."
	return render_template("index.html", headline=headline, paragraph=paragraph)

@app.route("/bye")
def bye():
	headline = "Good bye!"
	return render_template("index.html", headline=headline)