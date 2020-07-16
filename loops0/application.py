from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	fruits = ['Apple', 'Banana', 'Orange', 'Mango']  
	return render_template("index.html", fruits=fruits)
