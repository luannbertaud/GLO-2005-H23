import pymysql

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
        try:
            cursor = connection.cursor()
            request = f"INSERT INTO Likes (author, post_id, timestamp) VALUES ('{author}', '{post_id}', '{timestamp}');"
            cursor.execute(request)
        finally:
            connection.close()
