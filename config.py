import os

class Config:
    NEWS_API_BASE_URL ='https://newsapi.org/v1/articles?source={}&apiKey={}'
    NEWS_API_KEY = '7d93df81198e4704b7a7a1a88d2e652b'
    SECRET_KEY = 'tollysmith993'




class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    

config_options = {
'development':DevConfig,
'production':ProdConfig

}

