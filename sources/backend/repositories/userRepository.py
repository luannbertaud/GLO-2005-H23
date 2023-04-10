import pymysql
from uuid import uuid4

from exceptions.InvalidParameterException import InvalidParameterException


class UserRepository:

    def __int__(self):
        self.tokens = []

    @staticmethod
    def __create_connection() -> pymysql.Connection:
        return pymysql.connect(
            host="localhost",
            user="root",
            password="@Riane24",
            db="GLO_2005_H23",
            autocommit=True
        )

    def login(self, login_inputs):
        connection = self.__create_connection()
        email = login_inputs["email"]
        password = login_inputs["password"]
        try:
            cursor = connection.cursor()
            request = f"SELECT password FROM auth WHERE email = '{email}';"
            cursor.execute(request)
            hashed_password = cursor.fetchone()[0]
            if hashed_password is None:
                raise InvalidParameterException("email invalid")
            if sha256_crypt.verify(password, hashed_password):
                username = set.get_username_by_email(email)
                return {
                    "token_id": str(self.create_token(username)),
                    "username": public_DTO["username"]
                }
            else:
                raise InvalidParameterException("email or password invalid")
        finally:
            connection.close()

    def create_token(self, username):
        token_id = uuid4()
        token_creation_time = datetime.datetime.now()
        token_expire_time = datetime.datetime.now() + datetime.timedelta(days=1)
        new_token = {"token_id": token_id, "token_creation_time": token_creation_time,
                     "token_expire_time": token_expire_time, "username": username}
        self.tokens.append(new_token)
        return new_token["token_id"]

    def get_username_by_email(self, email):
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT username FROM Users WHERE email = '{email}';"
            cursor.execute(request)
            return cursor.fetchone()[0]
        finally:
            connection.close()
