from flask import render_template
from flask import request
from flask import redirect
from app import app

@app.route('/')
@app.route('/index', methods=["GET", "POST"])

def index():
	return render_template("base.html", title="Index")

@app.route('/first', methods=["GET", "POST"])
def first():
	print(request.headers)
	return render_template("BlueEyesWhiteDragon.html", title="First")

@app.route('/second', methods=["GET", "POST"])
def second():
	print(request.headers)
	return render_template("DarkMagician.html", title="Second")

@app.route('/third', methods=["GET", "POST"])
def third():
	print(request.headers)
	return render_template("Kuriboh.html", title="Third")
