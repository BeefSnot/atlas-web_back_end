#!/usr/bin/env python3
"""Users endpoints for API v1."""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_users():
    """List all User objects."""
    users = User.all()
    return jsonify([user.to_json() for user in users])

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Get a User object by ID."""
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())
