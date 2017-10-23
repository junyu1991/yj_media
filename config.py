import os

class Config:
    SECRET_KEY='test movie play'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG=True

    SQL_URI='mysql://root:test@192.168.1.101/development'

class TestingConfig(Config):
    TESTING=True
    SQL_URI='mysql://root:test@192.168.1.101/testing'

class ProductionConfig(Config):
    SQL_URI='mysql://root:test@192.168.1.101/production'


config={'development':DevelopmentConfig,
        'testing':TestingConfig,
        'production':ProductionConfig,
        'default':ProductionConfig
       }
