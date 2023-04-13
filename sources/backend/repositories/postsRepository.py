import pymysql

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
            request = f"SELECT * FROM Posts LIMIT {page*page_size}, {page*page_size+page_size};"
            cursor.execute(request)
            columns = [key[0] for key in cursor.description]
            posts = [dict(zip(columns, post)) for post in cursor.fetchall()]
        finally:
            connection.close()
        return posts
