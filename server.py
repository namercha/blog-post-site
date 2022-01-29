from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route('/guess/<string:name>')
def predict_age_and_gender(name):
    age_response = requests.get(url="https://api.agify.io/?name=" + name)
    age = age_response.json()["age"]
    gender_response = requests.get(url="https://api.genderize.io?name=" + name)
    gender = gender_response.json()["gender"]
    return render_template("answer.html", name=name.capitalize(), age=age, gender=gender)


if __name__ == '__main__':
    app.run(debug=True)
