from flask import Flask, request

import json
from repositories.userRepository import UserRepository
from services.auth import Auth

app = Flask(__name__)

user_repository = UserRepository()
auth = Auth(user_repository)

@app.route('/')
def heartbeat():
    return 'Welcome to InstaPaper API', 200


@app.route('/login', methods=['POST'])
def login():
    token = auth.login(request.get_json())
    return json.dumps(token), 200
    

if __name__ == '__main__':
    app.run()
