from flask import Flask, request

import json
from repositories.userRepository import UserRepository
from services.usersService import UsersService
from services.authService import AuthService

app = Flask(__name__)

user_repository = UserRepository()
users_service = UsersService(user_repository)
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
    result = users_service.create_user(request.get_json())
    return json.dumps({"userId": result}), 201


if __name__ == '__main__':
    app.run()
