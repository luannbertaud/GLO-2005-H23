import pymysql

from repositories.usersRepository import UsersRepository


class CommentsRepository:

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

    def get_comments_of_post(self, post_id: int):
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Comments AS c WHERE c.post_id = {post_id};"
            cursor.execute(request)
            columns = [key[0] for key in cursor.description]
            comments = [dict(zip(columns, com)) for com in cursor.fetchall()]
        finally:
            connection.close()
        return comments
