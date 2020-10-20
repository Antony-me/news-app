import newsapi
from app import app
import urllib.request,json
from .models import news
from newsapi import NewsApiClient

News = news.News

def get_news(headlines):

    newsapi =NewsApiClient(api_key='7d93df81198e4704b7a7a1a88d2e652b')

    headlines = newsapi.get_top_headlines(sources ="")

    return headlines


def get_bbc_news(headlines):

    newsapi =NewsApiClient(api_key='7d93df81198e4704b7a7a1a88d2e652b')

    headlines = newsapi.get_top_headlines(sources ="bbc-news")

    return headlines

def get_aljazeera_news(headlines):

    newsapi =NewsApiClient(api_key='7d93df81198e4704b7a7a1a88d2e652b')

    headlines = newsapi.get_top_headlines(sources ="al-jazeera-english")

    return headlines

# def get_search(keyword):

#     newsapi =NewsApiClient(api_key='7d93df81198e4704b7a7a1a88d2e652b')

#     headlines = newsapi.get("https://newsapi.org/v2/everything?q=bitcoin&apiKey=7d93df81198e4704b7a7a1a88d2e652b")

#     return headlines


def search_news(keyword):
    search_news_url = 'https://newsapi.org/v2/everything?q={}&apiKey=7d93df81198e4704b7a7a1a88d2e652b'.format(keyword)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_results = search_news_response

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_movie_results = process_results(search_news_list)




    return search_results


def process_results(headlines):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    search_results = []
    for items in headlines:
        title = items.get('title')
        description= items.get('description')
        urlToImage= items.get('urlToImage')
        content = items.get('content')
        publishedAt = items.get('publishedAt')
        source = items.get('source')


    return search_results


def get_abc_news(headlines):

    newsapi =NewsApiClient(api_key='7d93df81198e4704b7a7a1a88d2e652b')

    headlines = newsapi.get_top_headlines(sources ="abc-news")

    return headlines


