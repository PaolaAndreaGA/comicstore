from decouple import config


class Config:
    SECRET_KEY = 'Ahitienesucasapintada.'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'comicsworldstore'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
