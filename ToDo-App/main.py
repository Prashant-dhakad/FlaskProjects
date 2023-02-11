from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///db.sqlite3'
db = SQLAlchemy(app)



@app.route("/")
@app.route("/index")
def index():
    return render_template('dashboard/index.html')


@app.route("/about")
def about():
    return render_template('dashboard/about.html')






if __name__ == "__main__":
    app.run(debug=True)
