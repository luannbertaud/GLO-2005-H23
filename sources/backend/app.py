import json

from flask import Flask, request
from flask_cors import CORS
from asgiref.wsgi import WsgiToAsgi

from repositories.commentsRepository import CommentsRepository
from repositories.usersRepository import UsersRepository
from repositories.likesRepository import LikesRepository
from repositories.postsRepository import PostsRepository
from services.authService import AuthService
from services.commentsService import CommentsService
from services.postsService import PostsService
from services.usersService import UsersService
from services.likesService import LikesService

app = Flask(__name__)
CORS(app)
asgi_app = WsgiToAsgi(app)

user_repository = UsersRepository()
like_repository = LikesRepository(user_repository)
posts_repository = PostsRepository(user_repository)
comments_repository = CommentsRepository(user_repository)

user_service = UsersService(user_repository)
like_service = LikesService(user_repository, like_repository)
posts_service = PostsService(user_repository, posts_repository, comments_repository)
comments_service = CommentsService(user_repository, comments_repository)
auth_service = AuthService(user_repository)


@app.route('/')
def heartbeat():
    return 'Welcome to InstaPaper API', 200


# ----- Auth -----


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


@app.route('/verify_token', methods=['GET'])
def verify_token():
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    else:
        return 'Valid token', 200


# ----- User -----


@app.route('/profil/<string:username>', methods=['GET'])
def get_user_profil(username):
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    else:
        response = user_repository.get_user_profil_data(username)
    return json.dumps(response), 200


@app.route('/like', methods=['POST', 'DELETE'])
def like():
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    if request.method == 'POST':
        like_service.like(request.headers.get("X-token-id"), request.get_json())
        return "like successful", 200
    else:
        return 'Method not allowed', 405


@app.route('/search/<string:query>', methods=['GET'])
def search_user(query: str):
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    else:
        response = user_repository.search_user(query)
    return json.dumps(response), 200


# ----- Posts -----


@app.route('/posts', methods=['GET'])
def latest_posts():
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    res = posts_service.get_latest_posts(request.headers.get("X-token-id"), 0, 10)
    return json.dumps(res), 200


# ----- Comments -----


@app.route('/comments/<int:comment_id>', methods=['GET'])
def get_comment(comment_id: int):
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    return json.dumps(comments_service.get_comment_by_id(comment_id)), 200


@app.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id: int):
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    return comments_service.delete(request.headers.get("X-token-id"), comment_id)


@app.route('/comments', methods=['POST'])
def create_comment():
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    return comments_service.create(request.headers.get("X-token-id"), request.get_json()), 200


if __name__ == '__main__':
    app.run()
