from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts =[
        {'author' : {'username': "Ricardo"},
        'body' : "Some lipsum ipsum text"},
        {
            'author' : {'username': 'Serra'},
            'body' : "Some text"
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)