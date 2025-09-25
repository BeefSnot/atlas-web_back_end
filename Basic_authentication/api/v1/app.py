#!/usr/bin/env python3
"""Flask app for Basic Authentication project."""

from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None


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
    app.run(host=host, port=port)
