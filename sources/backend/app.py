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

# Declaration des dépots pour chaques relations.
users_repository = UsersRepository()
likes_repository = LikesRepository(users_repository)
posts_repository = PostsRepository(users_repository)
comments_repository = CommentsRepository(users_repository)
notif_repository = NotificationsRepository(users_repository)

# Nous utilisons des services pour gérer quelque logique pour les objets des relations.
users_service = UsersService(users_repository, likes_repository)
likes_service = LikesService(users_repository, likes_repository)
posts_service = PostsService(users_repository, posts_repository, comments_repository, likes_repository)
comments_service = CommentsService(users_repository, comments_repository)
auth_service = AuthService(users_repository)
notif_service = NotificationsService(users_repository, notif_repository)


@app.route('/')
def heartbeat():
    """
    Endpoint qui permet de savoir si l'API est bien fonctionnelle.
    :return: Toujours un message de succès et un code 200.
    """
    return 'Welcome to InstaPaper API', 200


# ----- Auth -----


@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint qui permet l'obtention d'un token d'authentification valide en échange d'un
    payload contenant un champ 'email' et un champ 'password'.
    :return: Le token d'authentification ou une InvalidParameterException.
    """
    token = auth_service.login(request.get_json())
    return json.dumps(token), 200


@app.route('/signup', methods=['POST'])
def signup():
    """
    Endpoint qui permet la création d'un compte utilisateur et l'obtention d'un token
    d'authentification valide en échange d'un payload contenant les champs
    'email', 'password' 'username', 'lastname' et 'bio'.
    :return: Le token d'authentification ou une InvalidParameterException.
    """
    token = users_service.create_user(request.get_json())
    return json.dumps(token), 201


@app.route('/logout', methods=['POST'])
def logout():
    """
    Endpoint qui supprime le token enregistré pour un certain utilisateur, ce qui confirme l'impossibilité
    de se connecter avec ce token.
    :return: Un message de succès et un code 200.
    """
    auth_service.logout(request.headers.get("X-token-id"))
    return 'Logout successful', 200


@app.route('/verify_token', methods=['GET'])
def verify_token():
    """
    Endpoint qui permet la vérification de la validité d'un token.
    :return: Un code 200 ou 401 suivant la validité du token.
    """
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    else:
        return 'Valid token', 200


# ----- User -----

@app.route('/profile/<string:username>', methods=['GET', 'DELETE'])
def get_user_profil(username):
    """
    Endpoint qui permet d'obtenir les informations sur un utilisateur en particulier.
    L'utilisateur doit être connecté pour accéder à cet endpoint.
    :param username: Le nom d'utilisateur du compte sur lequel nous souhaitons obtenir des informations.
    :return: Un json contenant les informations suivantes : 'username', 'email', 'firstname', 'lastname', 'bio'
    'following', 'followers', 'likes'.
    """
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    if request.method == 'GET':
        return json.dumps(users_service.get_user_info_by_username(username)), 200
    elif request.method == 'DELETE':
        logged_user = users_repository.get_user_by_token(request.headers.get("X-token-id"))
        return users_service.delete_user(request.headers.get("X-token-id"), logged_user)
    else:
        return 'Method not allowed', 405


@app.route('/like', methods=['POST', 'DELETE'])
def like():
    """
    Endpoint qui permet à un utilisateur de liker un post, ou de supprimer son like.
    :return: Un code 200 en cas de réussite, 401 si l'utilisateur
    n'est pas autorisé à faire cette action sur le Post demandé.
    """
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    if request.method == 'POST':
        return likes_service.like(request.headers.get("X-token-id"), request.get_json())
    elif request.method == 'DELETE':
        return likes_service.unlike(request.headers.get("X-token-id"), request.get_json())
    else:
        return 'Method not allowed', 405


@app.route('/post', methods=['POST'])
def create_post():
    """
    Endpoint qui permet à un utilisateur de créer un Post en son nom.
    Les champs requis sont 'author', 'body' et 'police'.
    :return: Un code 200 de succès ou une InvalidParameterException.
    """
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    return posts_service.post(request.headers.get("X-token-id"), request.get_json())


@app.route('/post/<string:post_id>', methods=['DELETE'])
def delete_post(post_id: str):
    """
    Endpoint qui permet à un utilisateur de supprimer un Post lui appartenant.
    :param post_id: L'id du post à supprimer.
    :return: Un code 200 de succès ou un code 400 si l'utilisateur n'est pas autorisé à supprimer ce Post.
    """
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    return posts_service.delete_post(request.headers.get("X-token-id"), post_id)


@app.route('/search/<string:query>', methods=['GET'])
def search_user(query: str):
    """
    Endpoint qui permet de recherche un utilisateur dont le nom d'utilisateur
    contient une certaine chaine de caractères.
    :param query: Chaine de caractères devant être contenue dans le nom d'utilisateur.
    :return: Un code 200 de succès et une liste des utilisateurs correspondant à la recherche.
    """
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    else:
        response = users_repository.search_user(query)
    return response, 200


# ----- Notifications -----


@app.route('/notifs', methods=['GET', 'PATCH'])
def get_last_notifs():
    """
    Endpoint qui permet à un utilisateur de récolter les notifications qui le concerne.
    Cette méthode permet aussi de changer le status d'une notification de 'unread' à 'read'.
    :return: Un code 200 avec un message de succès ou une InvalidParameterException.
    """
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    if request.method == 'GET':
        res = notif_service.get_last_notifs(request.headers.get("X-token-id"))
        return res, 200
    elif request.method == 'PATCH':
        if notif_service.set_read_notifs(request.headers.get("X-token-id")) is True:
            return 'Notifications marked as read', 200
        return 'Notifications have already been read', 200
    else:
        return 'Method not allowed', 405


# ----- Posts -----


@app.route('/posts', methods=['GET'])
def latest_posts():
    """
    Endpoint qui permet à un utilisateur récolter les derniers posts postés sur
    la plateforme de façon chronologique inverse.
    Deux paramètres peuvent être passés dans l'url de manière à gérer la pagination.
    Ex. GET .../posts?page=2&page_size=10
    :return: Une list des Posts contenu dans la page demandée.
    """
    page = request.args.get("page") or 0
    page_size = request.args.get("page_size") or 10
    page = int(page)
    page_size = int(page_size)
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    res = posts_service.get_latest_posts(request.headers.get("X-token-id"), page, page_size)
    return json.dumps(res), 200


@app.route('/posts/<string:username>', methods=['GET'])
def user_posts(username: str):
    """
    Endpoint qui permet à un utilisateur récolter les derniers posts postés par un utilisateur spécifique.
    :param username: Le nom d'utilisateur à qui doivent appartenir les Posts.
    :return: Une list des Posts appartenant à l'utilisateur.
    """
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    res = posts_service.get_posts_for_user(request.headers.get("X-token-id"), username)
    return json.dumps(res), 200


# ----- Comments -----


@app.route('/comments/<int:comment_id>', methods=['GET'])
def get_comment(comment_id: int):
    """
    Endpoint qui permet d'obtenir les informations d'un commentaire spécifique.
    Les données retournées sont : 'post_id', 'author', 'body', 'timestamp'.
    :param comment_id: L'id du commentaire ciblé.
    :return: Les données correspondantes au commentaire ciblé.
    """
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    return json.dumps(comments_service.get_comment_by_id(comment_id)), 200


@app.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id: int):
    """
    Endpoint permettant à un utilisateur de supprimé un commentaire lui appartenant.
    :param comment_id: L'id du commentaire à supprimer.
    :return: Code 200 en cas de succès, code 401 su l'utilisateur n'est pas autorisé à executer cette action.
    """
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    return comments_service.delete(request.headers.get("X-token-id"), comment_id)


@app.route('/comments', methods=['POST'])
def create_comment():
    """
    Endpoint qui permet à un utilisateur de créer un commentaire. Les données nécessaires sont :
    'post_id' et 'body'.
    :return: Les données du Post juste créé ou une InvalidParameterException.
    """
    if auth_service.is_token_valid(request.headers.get("X-token-id")) is False:
        return 'Invalid token', 401
    return comments_service.create(request.headers.get("X-token-id"), request.get_json()), 200


if __name__ == '__main__':
    app.run()
