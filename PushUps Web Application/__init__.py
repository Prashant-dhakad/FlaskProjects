from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
from .auth import auth as auth_blueprint
from .main import main as main_blueprint

app = Flask(__name__)
db = SQLAlchemy()

app.config['SECRETE_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# blueprint for auth routes in our app

app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
        
with app.app_context():
        db.init_app(app)
        db.create_all()
        
if __name__ == '__main__':
    app.run(debug = True)






