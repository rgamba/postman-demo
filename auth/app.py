from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def main():
    return jsonify({
        "service": "auth"
    })


@app.route("/authenticate", methods=["POST"])
def auth():
    """
    Accepts a POST with:
        - username
        - password
    """
    valid_users = {
        "admin": {
            "name": "Administrator",
            "pass": "admin"
        },
        "user": {
            "name": "Ricardo",
            "pass": "123"
        }
    }
    user = valid_users.get(request.form.get('username'))
    if not user or user['pass'] != request.form.get('password'):
        return jsonify({
            "error": "invalid credentials"
        }), 400
    return jsonify({
        "name": user['name']
    }), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)