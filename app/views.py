from types import new_class
from flask import render_template,request,redirect,url_for
from app import app


from .request import get_news

@app.route('/')
def index():
    '''
    docstring
    '''

    news = get_news('headlines')

    headline = news['articles']

    for items in news['articles']:

        title = items['title']
        description = items['description']

       
    # news = get_news('everything')

    # first= [news][0]

    # title = f'{news.title}'

    # urlToImage = []
    # description = []
    # content = []
    # url = []
    # publishedAt = []


    


    # for i in range(len(articles)):
    #     news_articles = articles[i]

    #     title.append(news_articles['title'])
    #     urlToImage.append(news_articles['urlToImage'])
    #     description.append(news_articles[description])
    #     content.append(news_articles[content])
    #     url.append(news_articles[url])
    #     publishedAt.append(news_articles[publishedAt])


    return render_template('index.html', headline = headline)