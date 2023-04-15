import json

from flask import Flask, request
from flask_cors import CORS
from asgiref.wsgi import WsgiToAsgi

from repositories.commentsRepository import CommentsRepository
from repositories.usersRepository import UsersRepository
from repositories.likesRepository import LikesRepository
from repositories.postsRepository import PostsRepository
from repositories.notificationsRepository import NotificationsRepository
from services.authService import AuthService
from services.commentsService import CommentsService
from services.postsService import PostsService
from services.usersService import UsersService
from services.likesService import LikesService
from services.notificationsService import NotificationsService

app = Flask(__name__)
CORS(app)
asgi_app = WsgiToAsgi(app)

users_repository = UsersRepository()
likes_repository = LikesRepository(users_repository)
posts_repository = PostsRepository(users_repository)
comments_repository = CommentsRepository(users_repository)
notif_repository = NotificationsRepository(users_repository)

users_service = UsersService(users_repository)
likes_service = LikesService(users_repository, likes_repository)
posts_service = PostsService(users_repository, posts_repository, comments_repository, likes_repository)
comments_service = CommentsService(users_repository, comments_repository)
auth_service = AuthService(users_repository)
notif_service = NotificationsService(users_repository, notif_repository)


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
    token = users_service.create_user(request.get_json())
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

@app.route('/profil/<string:username>', methods=['GET', 'DELETE'])
def get_user_profil(username):
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    if request.method == 'GET':
        return json.dumps(users_service.get_user_info_by_username(request.headers.get("X-token-id"), username)), 200
    elif request.method == 'DELETE':
        logged_user = users_repository.get_user_by_token(request.headers.get("X-token-id"))
        return users_service.delete_user(request.headers.get("X-token-id"), logged_user)
    else:
        return 'Method not allowed', 405


@app.route('/like', methods=['POST', 'DELETE'])
def like():
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    if request.method == 'POST':
        return likes_service.like(request.headers.get("X-token-id"), request.get_json())
    elif request.method == 'DELETE':
        return likes_service.unlike(request.headers.get("X-token-id"), request.get_json())
    else:
        return 'Method not allowed', 405


@app.route('/post', methods=['POST', 'DELETE'])
def post():
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    if request.method == 'POST':
        return posts_service.post(request.headers.get("X-token-id"), request.get_json())
    elif request.method == 'DELETE':
        return posts_service.delete_post(request.headers.get("X-token-id"), request.get_json())
    else:
        return 'Method not allowed', 405


@app.route('/search/<string:query>', methods=['GET'])
def search_user(query: str):
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    else:
        response = users_repository.search_user(query)
    return json.dumps(response), 200

# ----- Notifications -----

@app.route('/notifs', methods=['GET', 'PATCH'])
def get_last_notifs():
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    if request.method == 'GET':
        res = notif_service.get_last_notifs(request.headers.get("X-token-id"))
        return res, 200
    elif request.method == 'PATCH':
        if notif_service.set_read_notifs(request.headers.get("X-token-id")) is True:
            return 'Notifications marked as read', 200
        return 'Notifications have already been read', 400
    else:
        return 'Method not allowed', 405

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
