#!encoding:utf-8


from flask import Blueprint

movie_blueprint=Blueprint('movie',__name__)

from . import views
