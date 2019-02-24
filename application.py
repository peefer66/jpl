from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

####### CREATE DB ##########
db = SQLAlchemy()


def create_app():

    ########### APP ###########
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    ######### DATABASE ##############
    db.init_app(app)
    migrate = Migrate(app,db)
    

    ########## BLUEPRINTS ###########
    from core.views import core
    from customers.views import customer_blueprint

    app.register_blueprint(core)
    app.register_blueprint(customer_blueprint)


    return app 