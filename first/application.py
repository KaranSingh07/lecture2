from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/karan")
def karan():
	return "Hello, Karan!"

@app.route("/madhav")
def madhav():
	return "Hello, Madhav!"