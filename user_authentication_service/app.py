#!/usr/bin/env python3
"""
Flask app for user authentication service
"""
from flask import Flask, jsonify, request, abort, make_response
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
    # Get email and password from form data
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Validate login credentials
    if not AUTH.valid_login(email, password):
        abort(401)
    
    # Create session
    session_id = AUTH.create_session(email)
    
    # Prepare response
    response = make_response(jsonify({
        "email": email,
        "message": "logged in"
    }))
    
    # Set session cookie
    response.set_cookie('session_id', session_id)
    
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")