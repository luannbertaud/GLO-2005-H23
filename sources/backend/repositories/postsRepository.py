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
        connection = self.__create_connection()
        posts = []
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Posts ORDER BY timestamp DESC LIMIT {page*page_size}, {page*page_size+page_size};"
            cursor.execute(request)
            columns = [key[0] for key in cursor.description]
            posts = [dict(zip(columns, post)) for post in cursor.fetchall()]
        finally:
            connection.close()
        return posts

    def post(self, input_post):
        connection = self.__create_connection()
        author = input_post["author"]
        body = input_post["body"]
        police = input_post["police"]
        timestamp = input_post["timestamp"]
        try:
            cursor = connection.cursor()
            request = f"INSERT INTO Posts (author, body, police, timestamp)" \
                      f"VALUES ('{author}', '{body}', '{police}', '{timestamp}');"
            cursor.execute(request)
            return "Post successful", 200
        finally:
            connection.close()

    def is_post_already_exists(self, post_id):
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Posts WHERE id='{post_id}';"
            cursor.execute(request)
            return cursor.fetchone() is not None
        finally:
            connection.close()

    def delete_post(self, input_post):
        connection = self.__create_connection()
        post_id = input_post["post_id"]
        if self.is_post_already_exists(post_id) is True:
            try:
                cursor = connection.cursor()
                request = f"DELETE FROM Posts WHERE is='{post_id}';"
                cursor.execute(request)
                return "Delete post successful", 200
            finally:
                connection.close()
        else:
            raise InvalidParameterException("This post doesn't already exists")
