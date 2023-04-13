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

    def delete_comment(self, comment_id: int):
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"DELETE FROM Comments WHERE id = {comment_id};"
            affected_columns = cursor.execute(request)
        finally:
            connection.close()
        return affected_columns != 0

    def get_comment_by_id(self, comment_id):
        connection = self.__create_connection()
        comment = None
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Comments AS c WHERE c.id = {comment_id};"
            cursor.execute(request)
            columns = [key[0] for key in cursor.description]
            c_raw = cursor.fetchone()
            if c_raw is not None:
                comment = dict(zip(columns, c_raw))
        finally:
            connection.close()
        return comment
