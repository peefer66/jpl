from flask import Flask


def create_app():
    app = Flask(__name__)

    ########## BLUEPRINTS ###########

    from core.views import core

    app.register_blueprint(core)


    return app 