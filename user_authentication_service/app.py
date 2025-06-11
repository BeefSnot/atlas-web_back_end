#!/usr/bin/env python3
"""
Flask app for user authentication service
"""
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")