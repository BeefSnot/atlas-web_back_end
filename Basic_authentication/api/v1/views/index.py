#!/usr/bin/env python3
<<<<<<< HEAD
"""Index routes for Basic Authentication API."""
from flask import jsonify, abort
from api.v1.views import *
from api.v1.app import app

@app.route('/api/v1/status/', methods=['GET'])
def status():
    """Status endpoint."""
    return jsonify({"status": "OK"})

@app.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """Endpoint to trigger 401 error."""
    abort(401)

@app.route('/api/v1/forbidden', methods=['GET'])
def forbidden():
    """Endpoint to trigger 403 error."""
=======
"""Index and test endpoints for API v1."""

from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Health check endpoint."""
    return jsonify({"status": "OK"})


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    """Endpoint that triggers a 401 error."""
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden():
    """Endpoint that triggers a 403 error."""
>>>>>>> fb4997942433ff5d5191b7fd84256c4b7c006fa5
    abort(403)
