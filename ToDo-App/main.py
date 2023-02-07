from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class task(db.Model):
    id = db.column(db.Integer, primary_key = True)
    task = db.column(db.string(20), nullable = False, unique=True  )

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/insertask", methods=["POST","GET"])
def inserttask():
    if request.method=="POST":
        # get the task entered by the user for the form.
        enteredtask = request.form["todaystask"]
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
