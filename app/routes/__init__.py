"""
Routes package initialization.
This file makes the routes directory a Python package.
"""

from flask import Blueprint

api = Blueprint('api', __name__)
