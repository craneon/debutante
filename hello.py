from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/form")
def form():
    return render_template('form.html') 
    
@app.route("/submit", methods=['POST'])
def submit():
    return request.form["name"]

if __name__ == "__main__":
    app.run()