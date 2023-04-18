from datetime import datetime
import pymysql

from exceptions.InvalidParameterException import InvalidParameterException
from repositories.usersRepository import UsersRepository


class PostsRepository:

    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    @staticmethod
    def __create_connection() -> pymysql.Connection:
        return pymysql.connect(
            host="localhost",
            user="root",
            password="password",
            db="instapaper",
            autocommit=True
        )

    def get_latest_posts(self, page: int, page_size: int):
        """
        Méthode permettant d'obtenir les derniers posts de la plateforme par ordre chronologique inverse.
        Le résultat utilise de la pagination.
        :param page: Page actuelle à retourner de la pagination. Son origine dépend de la taille des pages.
        :param page_size: Taille des pages à considérer. Influence la taille de la liste de retour et l'origine de la
        page actuelle.
        :return: Liste des posts constituant la page demandée.
        """
        connection = self.__create_connection()
        posts = []
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Posts ORDER BY timestamp DESC LIMIT {page*page_size}, {page_size};"
            cursor.execute(request)
            columns = [key[0] for key in cursor.description]
            posts = [dict(zip(columns, post)) for post in cursor.fetchall()]
        finally:
            connection.close()
        return posts

    def post(self, input_post):
        """
        Méthode permettant de créer un post dans la base de données suivant les valeurs du payload passées en
        paramètre. Les valeurs nécessaires sont : 'author', 'body' et 'police'.
        :return: Un tuple contenant un message d'état et un code (200 pour un succès).
        """
        connection = self.__create_connection()
        author = input_post["author"]
        body = input_post["body"]
        police = input_post["police"]
        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        try:
            cursor = connection.cursor()
            request = f"INSERT INTO Posts (author, body, police, timestamp)" \
                      f"VALUES ('{author}', '{body}', '{police}', '{timestamp}');"
            cursor.execute(request)
            return "Post successful", 200
        finally:
            connection.close()

    def is_post_already_exists(self, post_id):
        """
        Méthode permettant de savoir si un post existe suivant un id.
        :param post_id: Id du post recherché.
        :return: Un boolean signifiant si oui ou non le post existe.
        """
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Posts WHERE id='{post_id}';"
            cursor.execute(request)
            return cursor.fetchone() is not None
        finally:
            connection.close()

    def delete_post(self, username, post_id):
        """
        Supprime un post dans la base de données.
        :param username: Nom d'utilisateur de l'auteur du post. (Pour des raisons de sécurité).
        :param post_id: L'id avec lequel identifier le commentaire à supprimer.
        :return: Un tuple contenant un message d'état et un code (200 pour un succès).
        """
        connection = self.__create_connection()
        if self.is_post_already_exists(post_id) is True:
            try:
                cursor = connection.cursor()
                request = f"DELETE FROM Posts WHERE id='{post_id}' AND author='{username}';"
                success = cursor.execute(request) != 0
                if success:
                    return "Delete post successful", 200
                return "Post does not belong to requesting user", 400
            finally:
                connection.close()
        else:
            raise InvalidParameterException("This post doesn't already exists")

    def get_posts_of_user(self, username):
        """
        Méthode permettant d'obtenir une liste des posts d'un utilisateur par ordre chronologique inverse.
        :param username: Nom d'utilisateur pour qui rechercher les posts publiés.
        :return: Une liste des posts de l'utilisateur demandé.
        """
        connection = self.__create_connection()
        posts = []
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Posts WHERE author='{username}' ORDER BY timestamp DESC;"
            cursor.execute(request)
            columns = [key[0] for key in cursor.description]
            posts = [dict(zip(columns, post)) for post in cursor.fetchall()]
        finally:
            connection.close()
        return posts
