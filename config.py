from decouple import config


class Config:
    SECRET_KEY='Andrea8727.'


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
