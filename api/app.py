from __future__ import print_function

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


POSTMAN_URL = "http://api_postman:8130"
AUTH_SERVICE = "auth"


@app.route("/")
def main():
    return jsonify({
        "service": "api"
    })


@app.route("/status")
def status():
    """
    Expects Authentication header with username and password.
    """
    user = get_user()
    if not user:
        return jsonify({
            "error": "invalid credentials"
        }), 400
    return jsonify({
        "message": "Welcome, {}!".format(user['name']),
    })


def get_user():
    auth = request.authorization
    return authenticate(auth.username, auth.password)


def authenticate(username, password):
    response = requests.post("{}/{}/authenticate".format(POSTMAN_URL, AUTH_SERVICE), {
        "username": username,
        "password": password
    })
    if response.status_code != 200:
        return None
    return response.json()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)