from flask import Flask, render_template

from flask_joke import joke, joke_from_json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', joke=joke())


@app.route('/from_json')
def from_json():
    return render_template('index.html', joke=joke_from_json())
