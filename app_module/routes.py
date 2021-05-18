from flask import request
from flask import render_template
from app_module import app
from app_module import trans


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search')
def search():
    word = request.args.get('word')
    if not trans.get(str(word)):
        return render_template('warn.html')
    return render_template('index.html', word=trans[str(word)])
