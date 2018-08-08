from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
	return render_template(
		"home.html")
@app.route('/student/<int:id>')
def nevigate (id):
	return render_template(
		"home.html" , id = id )
app.run(debug=True)
