# import os


# class Config:
#     '''
#     General configuration parent class
#     '''
#     ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
#     NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
#     NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
#     SECRET_KEY = os.environ.get('SECRET_KEY')


# class ProdConfig(Config):
#         '''
#         Production  configuration child class

#         Args:
#             Config: The parent configuration class with General configuration settings
#         '''
#         pass


# class DevConfig(Config):
#         '''
#         Development  configuration child class

#         Args:
#             Config: The parent configuration class with General configuration settings
#         '''
#         DEBUG = True


# config_options = {
#     'development': DevConfig,
#     'production': ProdConfig
# }




import os

class Config:

   	NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
   	ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
   	NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
   
   	pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}