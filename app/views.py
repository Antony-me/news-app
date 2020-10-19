from flask import Flask, render_template
from app import app


from .request import get_news

@app.route('/')
def index():
    pass
    '''
    docstring
    '''



    return render_template('index.html', )