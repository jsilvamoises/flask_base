from flask import Flask
from config import app_config,DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()



def create_app(config_name):

    app = Flask(__name__,instance_relative_config=True)
    cfg = DevelopmentConfig()
    cfg.init_app(app)
    app.config.from_object(cfg)
    
    db.init_app(app)
    migrate = Migrate(app, db)
   
   

    db.init_app(app)
    migrate.init_app(app,db)
    login.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .errors import errors as error_blueprint
    app.register_blueprint(error_blueprint)

    return app
