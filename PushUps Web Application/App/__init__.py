from flask import  Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

from .auth import auth as auth_blueprint
from .main import main as main_blueprint

app.config['SECRETE_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
        db.init_app(app)
        db.create_all()

# blueprint for auth routes in our app
#from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
#from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
        
        
if __name__ == '__main__':
    app.run(debug = True)






