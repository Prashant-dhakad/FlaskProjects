from flask import  Flask
from auth import auth
from main import main


app = Flask(__name__)
    

app.register_blueprint(auth)
app.register_blueprint(main)
        

if __name__ == '__main__':
    app.run(debug = True)






