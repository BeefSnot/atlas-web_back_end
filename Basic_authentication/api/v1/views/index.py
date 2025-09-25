#!/usr/bin/env python3
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
    abort(403)
