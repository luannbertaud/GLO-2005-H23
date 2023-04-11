from flask import Flask, request

import json
from sources.backend.users import Users
from sources.backend.auth import Auth

app = Flask(__name__)

user = Users()
auth = Auth()


@app.route('/')
def heartbeat():
    return 'Welcome to InstaPaper API', 200


@app.route('/login', methods=['POST'])
def login():
    token = auth.login(request.get_json())
    return json.dumps(token), 200


@app.route('/signup', methods=['POST'])
def signup():
    result = user.create_user(request.get_json())
    return json.dumps({"userId": result}), 201


if __name__ == '__main__':
    app.run()
