from app import app
import urllib.request,json
from .models import news
from newsapi import NewsApiClient

News = news.News

def get_news(everything):

    newsapi =NewsApiClient(api_key='7d93df81198e4704b7a7a1a88d2e652b')

    data = newsapi.get_everything(q= 'jupyter lab', language= 'en', page_size=20)


    news_articles = data['articles']


    return news_articles

