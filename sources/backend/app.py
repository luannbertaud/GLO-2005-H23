import json

from flask import Flask, request

from sources.backend.repositories.usersRepository import UsersRepository
from sources.backend.repositories.likesRepository import LikesRepository
from sources.backend.repositories.postsRepository import PostsRepository
from sources.backend.services.authService import AuthService
from sources.backend.services.usersService import UsersService
from sources.backend.services.likesService import LikesService
from sources.backend.services.postsService import PostsService

app = Flask(__name__)

user_repository = UsersRepository()
post_repository = PostsRepository(user_repository)
like_repository = LikesRepository(user_repository)
user_service = UsersService(user_repository)
like_service = LikesService(user_repository, like_repository)
post_service = PostsService(user_repository, post_repository)

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


@app.route('/like', methods=['POST', 'DELETE'])
def like():
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    if request.method == 'POST':
        return like_service.like(request.headers.get("X-token-id"), request.get_json())
    elif request.method == 'DELETE':
        return like_service.unlike(request.headers.get("X-token-id"), request.get_json())
    else:
        return 'Method not allowed', 405


@app.route('/post', methods=['POST', 'DELETE'])
def post():
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    if request.method == 'POST':
        return post_service.post(request.headers.get("X-token-id"), request.get_json())
    elif request.method == 'DELETE':
        return post_service.delete_post(request.headers.get("X-token-id"), request.get_json())
    else:
        return 'Method not allowed', 405


if __name__ == '__main__':
    app.run()
