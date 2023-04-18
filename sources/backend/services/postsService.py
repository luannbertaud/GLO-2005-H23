import time

from exceptions.MissingParameterException import MissingParameterException
from repositories.commentsRepository import CommentsRepository
from repositories.likesRepository import LikesRepository
from repositories.postsRepository import PostsRepository
from repositories.usersRepository import UsersRepository


class PostsService:

    def __init__(self, user_repository: UsersRepository, posts_repository: PostsRepository,
                 comments_repository: CommentsRepository, likes_repository: LikesRepository):
        self.user_repository = user_repository
        self.posts_repository = posts_repository
        self.comments_repository = comments_repository
        self.likes_repository = likes_repository

    def get_latest_posts(self, token_id, page: int, page_size: int):
        """
        Méthode permettant de sélectionner une liste de Posts dans un ordre chronologique inverse.
        :param token_id: Le token de l'utilisateur faisant la requête.
        :param page: La page actuelle de la requête, ignorant les Posts précédants et suivants.
        :param page_size: La taille des pages à considérer (influence la taille de la liste de retour et son
        point de commencement).
        :return: Une liste des Posts correspondants à la page demandée.
        """
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        query_res = self.posts_repository.get_latest_posts(page, page_size)
        for post in query_res:
            post["timestamp"] = time.mktime(post["timestamp"].timetuple())
            post["comments"] = self.comments_repository.get_comments_of_post(post["id"])
            post["likes"] = self.likes_repository.count_likes_of_post(post["id"])
            post["user_like"] = self.likes_repository.is_like_already_exists(
                self.user_repository.get_user_by_token(token_id), post["id"])
            for com in post["comments"]:
                com["timestamp"] = time.mktime(com["timestamp"].timetuple())
        return query_res

    def post(self, token_id, input_post):
        """
        Méthode créant un Post dans la base de données après avoir vérifié le droit de l'utilisateur à créer ce Post.
        :param token_id: Le token de l'utilisateur faisant la requête.
        :param input_post: Paylod contenant les différentes données nécessaires à la création d'un Post.
        :return: Un code 200 de succès ou un code 401 si l'utilisateur n'est pas autorisé à exécuter cette requête.
        """
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        if self.user_repository.get_user_by_token(token_id) == input_post["author"]:
            return self.posts_repository.post(input_post)
        else:
            return 'Unauthorized', 401

    def delete_post(self, token_id, post_id):
        """
        Méthode supprimant un Post après avoir vérifié s'il existe.
        :param token_id: Le token de l'utilisateur faisant la requête.
        :param post_id: L'id du Post à supprimer.
        :return: Un code 200 en cas de succès, un code 400 en cas de non-autorisation.
        """
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        username = self.user_repository.get_user_by_token(token_id)
        return self.posts_repository.delete_post(username, post_id)

    def get_posts_for_user(self, token_id, username: str):
        """
        Méthode permettant de récolter les posts postés par un utilisateur spécifique.
        :param token_id: Le token de l'utilisateur faisant la requête.
        :param username: Le nom d'utilisateur à qui doivent appartenir les Posts.
        :return: Une list des Posts appartenant à l'utilisateur.
        """
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        query_res = self.posts_repository.get_posts_of_user(username)
        for post in query_res:
            post["timestamp"] = time.mktime(post["timestamp"].timetuple())
            post["comments"] = self.comments_repository.get_comments_of_post(post["id"])
            post["likes"] = self.likes_repository.count_likes_of_post(post["id"])
            post["user_like"] = self.likes_repository.is_like_already_exists(
                self.user_repository.get_user_by_token(token_id), post["id"])
            for com in post["comments"]:
                com["timestamp"] = time.mktime(com["timestamp"].timetuple())
        return query_res
