#imports from third party
from flask import Flask

#local imports
from config import shopping_app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(shopping_app_config[config_name])
    app.config.from_pyfile('config.py')

    #temp route
    @app.route('/')
    def hello_world():
        return 'Hello world'

    return app