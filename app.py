import os
from flask import Flask, request, render_template
app = Flask(__name__)

import biogenerator
from biogenerator import biogenerate

@app.route("/")
def hello():
    return render_template("form.html")
    
@app.route("/submit", methods=['POST'])
def submit():
	name = request.form["name"]
	age = request.form["age"]
	return render_template("submit.html",
		name = name,
		bio = biogenerate(name, age))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)