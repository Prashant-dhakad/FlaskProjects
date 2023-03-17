from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from flask_login import LoginManager
import flask_login
import flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
        db.init_app(app)
        db.create_all()

login_manager = flask_login.LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from models import User, db
@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))

# blueprint for auth routes in our app
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from main import main as main_blueprint
app.register_blueprint(main_blueprint)
        
        
if __name__ == '__main__':
    app.run(debug = True)






