import json

from flask import Flask, request

from sources.backend.repositories.usersRepository import UsersRepository
from sources.backend.services.authService import AuthService
from sources.backend.services.usersService import UsersService

app = Flask(__name__)

user_repository = UsersRepository()
user_service = UsersService(user_repository)
auth_service = AuthService(user_repository)


@app.route('/')
def heartbeat():
    return 'Welcome to InstaPaper API', 200


@app.route('/login', methods=['POST'])
def login():
    token = auth_service.login(request.get_json())
    return json.dumps(token), 200


@app.route('/signup', methods=['POST'])
def signup():
    token = user_service.create_user(request.get_json())
    return json.dumps(token), 201


@app.route('/logout', methods=['POST'])
def logout():
    auth_service.logout(request.headers.get("X-token-id"))
    return 'Logout successful', 200


@app.route('/profil/<string:username>', methods=['GET'])
def get_user_profil(username):
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    else:
        response = user_repository.get_user_profil_data(username)
    return json.dumps(response), 200


@app.route('/verify_token', methods=['GET'])
def verify_token():
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    else:
        return 'Valid token', 200


if __name__ == '__main__':
    app.run()
