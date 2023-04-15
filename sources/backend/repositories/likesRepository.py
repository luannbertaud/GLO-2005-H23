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
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Likes WHERE author='{author}' AND post_id={post_id};"
            cursor.execute(request)
            return cursor.fetchone() is not None
        finally:
            connection.close()

    def unlike(self, author, post_id):
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
