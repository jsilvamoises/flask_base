import os
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):   
    SECRET_KEY = os.environ.get('SECRET_KEY','P@R14B1')

    MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT','587'))
    MAIL_USE_TSL = os.environ.get('MAIL_USE_TSL','true').lower() in ['true','on','1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    FLASK_MAIL_SUBJECT_PREFIX = '[BI]'
    FLASK_MAIL_SENDER = 'BI<bi@fenix.com.br>'
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
    f"sqlite:///{os.path.join(base_dir,'app.sqlite3')}")

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
    f"sqlite:///{os.path.join(base_dir,'app_teste.sqlite3')}")

class ProdutionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
    f"sqlite:///{os.path.join(base_dir,'prodution.sqlite3')}")




app_config = {
        'development': DevelopmentConfig,
        'testing':TestingConfig,
        'production': ProdutionConfig,
        'default':DevelopmentConfig
}



    
    



