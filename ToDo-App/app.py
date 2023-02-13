from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///sqlite.db'
db = SQLAlchemy(app)

#Create Models
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean, default = False)

@app.route("/")
@app.route("/index")
def index():
    return render_template('dashboard/index.html')


@app.route("/add")
def add():
    return render_template(url_for('index'))



@app.route("/about")
def about():
    return render_template('dashboard/about.html')






if __name__ == "__main__":
    app.run(debug=True)
