#!/usr/bin/env python3
"""Flask application for the user authentication service.

Exposes routes for registration, login/logout via session cookies,
profile retrieval, and password reset flows.
"""
from __future__ import annotations

from typing import Tuple

from flask import Flask, Response, abort, jsonify, redirect, request

try:
    from .auth import Auth
except Exception:
    from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> Response:
    """Root endpoint returning a welcome message."""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> Response:
    """Register a new user from form data (email, password)."""
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        return jsonify({"message": "email and password required"}), 400
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": user.email, "message": "user created"})


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> Response:
    """Log a user in, set session cookie, and return confirmation JSON."""
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password or not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    if session_id is None:
        abort(401)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> Response:
    """Log a user out if a valid session exists; otherwise 403."""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> Response:
    """Return the email for a valid session, else 403."""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    return jsonify({"email": user.email})


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> Response:
    """Return a reset token for a valid email, else 403."""
    email = request.form.get("email")
    if not email:
        abort(403)
    try:
        token = AUTH.get_reset_password_token(email)
    except Exception:
        abort(403)
    return jsonify({"email": email, "reset_token": token})


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password() -> Response:
    """Update a user's password given a valid reset token; else 403."""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    if not email or not reset_token or not new_password:
        abort(403)
    try:
        AUTH.update_password(reset_token, new_password)
    except Exception:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
