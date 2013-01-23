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
	name1 = request.form["name1"]
	name2 = request.form["name2"]
	age = request.form["age"]
	return render_template("submit.html",
		name1 = name1,
		name2 = name2,
		bio = biogenerate(name1, name2, age))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)