from flask import Flask, render_template
from newsapi import NewsApiClient


app = Flask(__name__)

@app.route('/')
def Index():
    newsapi =NewsApiClient(api_key="7d93df81198e4704b7a7a1a88d2e652b")
    topheadlines = newsapi.get_top_headlines(sources ="bbc-news")
    """
    docstring
    """
    articles =topheadlines['articles']

    desc =[]
    news = []
    img =[]


    for i in range(len(articles)):
        myarticles = articles[i]


        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render_template('index', context = mylist)
