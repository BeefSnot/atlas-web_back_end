#!/usr/bin/env python3
<<<<<<< HEAD
"""Views package init file."""
=======
"""Blueprint setup for API v1 views."""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
>>>>>>> fb4997942433ff5d5191b7fd84256c4b7c006fa5
