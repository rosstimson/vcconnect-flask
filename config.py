import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environb.get(b'SECRET_KEY')
    VCC_API_KEY = os.environ.get('VCC_API_KEY')


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


# class ProductionConfig(Config):


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    # 'production': ProductionConfig,

    'default': DevelopmentConfig
}
