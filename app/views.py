from types import new_class
from flask import render_template,request,redirect,url_for
from app import app



from .request import get_abc_news, get_aljazeera_news, get_bbc_news, get_news, search_news

@app.route('/')
def index():
    '''
    docstring
    '''

    news = get_news('headlines')

    headline = news['articles']

    search_news = request.args.get('news_query')

    if search_news:

        return redirect(url_for('search',keyword =search_news))
    else:

        return render_template('index.html', headline = headline)


@app.route('/search/<keyword>')
def search(keyword):
    '''
    View function to display the search results
    '''
    news_name_list =keyword.split(" ")
  
    searched_news = search_news(keyword)

    title = f'SEARCH RESULT FOR   {news_name_list}'
    
    return render_template('search.html',title = title, news = searched_news)





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


@app.route('/abc')
def abc():

    abc = get_abc_news('headlines')
    abc = abc['articles']


    return render_template('abc.html', headline = abc)


