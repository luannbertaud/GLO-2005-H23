from datetime import datetime

import pymysql

from exceptions.InvalidParameterException import InvalidParameterException
from repositories.usersRepository import UsersRepository


class LikesRepository:

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

    def like(self, author, post_id):
        """
        Méthode permettant de créer un like dans la base de données suivant les valeurs passées en
        paramètre. Toutes les valeurs en paramètre sont nécessaires.
        :return: Un boolean indiquant si le like a été créé.
        """
        connection = self.__create_connection()
        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        if self.is_like_already_exists(author, post_id) is False:
            try:
                cursor = connection.cursor()
                request = f"INSERT INTO Likes (author, post_id, timestamp)" \
                          f"VALUES ('{author}', '{post_id}', '{timestamp}');"
                return cursor.execute(request) != 0
            finally:
                connection.close()
        else:
            raise InvalidParameterException('This post is already like by this user')

    def is_like_already_exists(self, author, post_id):
        """
        Méthode permettant de savoir si un like existe suivant l'auteur de ce like et un post cible.
        :param author: Username de l'auteur du like recherché.
        :param post_id: Id du post qui aurait été liké par l'auteur.
        :return: Un boolean signifiant si oui ou non le like existe.
        """
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Likes WHERE author='{author}' AND post_id={post_id};"
            cursor.execute(request)
            return cursor.fetchone() is not None
        finally:
            connection.close()

    def unlike(self, author, post_id):
        """
        Méthode permettant de supprimer un like dans la base de données suivant les valeurs passées en
        paramètre. Toutes les valeurs en paramètre sont nécessaires.
        :return: Un boolean indiquant si le like a été supprimé.
        """
        connection = self.__create_connection()
        if self.is_like_already_exists(author, post_id) is True:
            try:
                cursor = connection.cursor()
                request = f"DELETE FROM Likes WHERE author='{author}' AND post_id={post_id};"
                return cursor.execute(request) != 0
            finally:
                connection.close()
        else:
            raise InvalidParameterException('This post is not already liked by this user')

    def count_likes_of_post(self, post_id):
        """
        Méthode permettant d'obtenir le nombre de likes d'un post en particulier.
        :param post_id: L'id du post sur lequel compter les likes.
        :return: Le nombre de likes en relation avec le post.
        """
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT COUNT(id) FROM Likes WHERE post_id={post_id};"
            cursor.execute(request)
            count = cursor.fetchone()
            if count is None or len(count) <= 0:
                return 0
            return count[0]
        finally:
            connection.close()

    def count_likes_for_user(self, username):
        """
        Méthode permettant d'obtenir le nombre de likes cumulés de tous les posts d'un utilisateur.
        :param username: Le nom d'utilisateur pour qui compter le nombre de likes.
        :return: Le nombre de likes cumulés des posts de l'utilisateur.
        """
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT COUNT(l.id) FROM Likes as l, Posts as p" \
                      f" WHERE l.post_id = p.id AND p.author = '{username}';"
            cursor.execute(request)
            count = cursor.fetchone()
            if count is None or len(count) <= 0:
                return 0
            return count[0]
        finally:
            connection.close()
