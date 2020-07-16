from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/fruits")
def show_fruits():
	fruits = ['Apple', 'Banana', 'Orange', 'Mango']  
	return render_template("list.html", list=fruits, list_title="Fruits")

@app.route("/veggies")
def show_veggies():
	veggies = ['Tomato', 'Onion', 'Tomato', 'Brinjal']
	return render_template("list.html", list=veggies, list_title="Veggies")

@app.route("/spices")
def show_spices():
	spices = ['Termeric', 'Salt', 'Black pepper', 'Chilli powder']
	return render_template("list.html", list=spices, list_title="Spices")