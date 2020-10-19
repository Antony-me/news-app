from app import app
import urllib.request,json
from .models import news
from newsapi import NewsApiClient

News = news.News

def get_news(headlines):

    newsapi =NewsApiClient(api_key='7d93df81198e4704b7a7a1a88d2e652b')

    headlines = newsapi.get_top_headlines(sources ="bbc-news")

    return headlines

