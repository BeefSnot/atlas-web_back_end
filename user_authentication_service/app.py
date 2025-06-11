#!/usr/bin/env python3
"""
Flask app for user authentication service
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def welcome():
    """
    Basic route that returns a welcome message
    
    Returns:
        JSON response with welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """
    Register a new user
    
    Expects form data with 'email' and 'password' fields
    
    Returns:
        JSON response with registration status
    """
    email = request.form.get('email')
    password = request.form.get('password')
    
    try:
        user = AUTH.register_user(email, password)
        return jsonify({
            "email": email,
            "message": "user created"
        })
    except ValueError:
        return jsonify({
            "message": "email already registered"
        }), 400


@app.route('/sessions', methods=['POST'])
def login():
    """
    Login a user and create a new session
    
    Expects form data with 'email' and 'password' fields
    
    Returns:
        JSON response with login status and sets session cookie
    """
    email = request.form.get('email')
    password = request.form.get('password')
    
    if not AUTH.valid_login(email, password):
        abort(401)
    
    session_id = AUTH.create_session(email)
    
    response = make_response(jsonify({
        "email": email,
        "message": "logged in"
    }))
    
    response.set_cookie('session_id', session_id)
    
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """
    Log out a user by destroying their session
    
    Expects a session_id cookie
    
    Returns:
        Redirect to home page if successful, 403 otherwise
    """
    session_id = request.cookies.get('session_id')
    
    user = AUTH.get_user_from_session_id(session_id)
    
    if user is None:
        abort(403)
    
    AUTH.destroy_session(user.id)
    
    return redirect('/')


@app.route('/profile', methods=['GET'])
def profile():
    """
    Get user profile information
    
    Expects a session_id cookie
    
    Returns:
        JSON with user email if session is valid, 403 otherwise
    """
    session_id = request.cookies.get('session_id')
    
    user = AUTH.get_user_from_session_id(session_id)
    
    if user is None:
        abort(403)
    
    return jsonify({"email": user.email})


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """
    Request a password reset token
    
    Expects form data with 'email' field
    
    Returns:
        JSON with email and reset token if email exists, 403 otherwise
    """
    email = request.form.get('email')
    
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({
            "email": email,
            "reset_token": reset_token
        })
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """
    Update a user's password using a reset token
    
    Expects form data with 'email', 'reset_token', and 'new_password' fields
    
    Returns:
        JSON with success message if token is valid, 403 otherwise
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    
    try:
        AUTH.update_password(reset_token, new_password)
        
        return jsonify({
            "email": email,
            "message": "Password updated"
        })
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
