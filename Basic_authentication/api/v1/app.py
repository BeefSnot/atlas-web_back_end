#!/usr/bin/env python3
<<<<<<< HEAD
"""Flask app for Basic Authentication API."""
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os
=======
"""Flask app for Basic Authentication project."""

from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
>>>>>>> fb4997942433ff5d5191b7fd84256c4b7c006fa5

app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
<<<<<<< HEAD
AUTH_TYPE = os.getenv('AUTH_TYPE')
if AUTH_TYPE == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif AUTH_TYPE == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()

@app.errorhandler(401)
def unauthorized_error(error):
    """Handler for 401 Unauthorized errors."""
    return jsonify({"error": "Unauthorized"}), 401

@app.errorhandler(403)
def forbidden_error(error):
    """Handler for 403 Forbidden errors."""
    return jsonify({"error": "Forbidden"}), 403

@app.before_request
def before_request_func():
    """Filter requests before handling them."""
    if auth is None:
        return
    excluded = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if not auth.require_auth(request.path, excluded):
        return
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)

from api.v1.views import *

if __name__ == "__main__":
    host = os.getenv('API_HOST', '0.0.0.0')
    port = int(os.getenv('API_PORT', 5000))
=======


def get_auth_instance():
    """Return an auth instance based on AUTH_TYPE env variable."""
    global auth
    auth_type = getenv("AUTH_TYPE")
    if auth_type == "basic_auth":
        from api.v1.auth.basic_auth import BasicAuth

        auth = BasicAuth()
    elif auth_type == "auth":
        from api.v1.auth.auth import Auth

        auth = Auth()
    else:
        auth = None


@app.before_request
def before_request() -> None:
    """Filter requests using auth if configured."""
    global auth
    if auth is None:
        return
    from api.v1.auth.auth import Auth

    excluded = [
        "/api/v1/status/",
        "/api/v1/unauthorized/",
        "/api/v1/forbidden/",
    ]
    if auth.require_auth(request.path, excluded):
        if auth.authorization_header(request) is None:
            abort(401)
        if auth.current_user(request) is None:
            abort(403)


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error):
    return jsonify({"error": "Forbidden"}), 403


from api.v1.views import app_views

app.register_blueprint(app_views)


if __name__ == "__main__":
    get_auth_instance()
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
>>>>>>> fb4997942433ff5d5191b7fd84256c4b7c006fa5
    app.run(host=host, port=port)
