from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/<int:id>')
def home (id):
	return render_template(
		"home.html" , 
		id = id )

@app.route('/student/<int:id>')
def route(id):
	return render_template(
		'student.html',
		 student_id=id)
app.run(debug=True)

