from flask import Flask, render_template
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def home():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city = 'Las vegas'
    
    r = requests.get(url.format(city)).json()
   
    
    weather = {
            'city' : 'city',
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)