#!encoding:utf-8

from flask import Flask

from config import config


def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    from .movie import movie_blueprint

    app.register_blueprint(movie_blueprint,url_prefix='/movie')

    return app
