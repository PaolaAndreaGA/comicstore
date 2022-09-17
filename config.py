from decouple import config


class Config:
    SECRET_KEY = 'Ahitienesucasapintada.'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'comicsworldstore'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
