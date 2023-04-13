import pymysql
from sources.backend.exceptions.InvalidParameterException import InvalidParameterException
from sources.backend.repositories.usersRepository import UsersRepository


class LikesRepository:

    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    @staticmethod
    def __create_connection() -> pymysql.Connection:
        return pymysql.connect(
            host="localhost",
            user="root",
            password="@Riane24",
            db="GLO_2005_H23",
            autocommit=True
        )

    def like(self, input_like):
        connection = self.__create_connection()
        author = input_like["author"]
        post_id = input_like["post_id"]
        timestamp = input_like["timestamp"]
        if self.is_like_already_exists(author, post_id) is False:
            try:
                cursor = connection.cursor()
                request = f"INSERT INTO Likes (author, post_id, timestamp) VALUES ('{author}', '{post_id}', '{timestamp}');"
                cursor.execute(request)
                return "Like successful", 200
            finally:
                connection.close()
        else:
            raise InvalidParameterException('This post is already like by this user')

    def is_like_already_exists(self, author, post_id):
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Likes WHERE author='{author}' AND post_id={post_id};"
            cursor.execute(request)
            return cursor.fetchone() is not None
        finally:
            connection.close()

    def unlike(self, input_like):
        connection = self.__create_connection()
        author = input_like["author"]
        post_id = input_like["post_id"]
        if self.is_like_already_exists(author, post_id) is True:
            try:
                cursor = connection.cursor()
                request = f"DELETE FROM Likes WHERE author='{author}' AND post_id={post_id};"
                cursor.execute(request)
                return "UnLike successful", 200
            finally:
                connection.close()
        else:
            raise InvalidParameterException('This post is not already like by this user')
