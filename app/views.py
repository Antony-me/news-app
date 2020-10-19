from types import new_class
from flask import render_template,request,redirect,url_for
from app import app


from .request import get_aljazeera_news, get_bbc_news, get_news

@app.route('/')
def index():
    '''
    docstring
    '''

    news = get_news('headlines')

    headline = news['articles']

    return render_template('index.html', headline = headline)

@app.route('/bbc')
def bbc():

    bbc = get_bbc_news('headlines')
    bbc_news =  bbc['articles']
    


    return render_template('bbc.html', headline = bbc_news )

@app.route('/aljazeera')
def aljazeera():

    aljazeera = get_aljazeera_news('headlines')
    aljazeera =  aljazeera['articles']


    return render_template('aljazeera.html', headline = aljazeera)

