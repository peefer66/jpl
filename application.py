from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

####### CREATE DB ##########
db = SQLAlchemy()

login_manager = LoginManager()



def create_app():

    ########### APP ###########
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    ######### DATABASE ##############
    db.init_app(app)
    migrate = Migrate(app,db)

    ######### LOGIN ################
    
    login_manager.init_app(app)
    login_manager.login_view = 'user_bp.login'
        

    ########## BLUEPRINTS ###########
    from core.views import core_bp
    from customers.views import customer_bp
    from compounds.views import compound_bp
    from users.views import user_bp

    app.register_blueprint(core_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(compound_bp)
    app.register_blueprint(user_bp)


    return app 