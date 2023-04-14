import pymysql
from uuid import uuid4, UUID
from passlib.hash import sha256_crypt
import datetime

from exceptions.InvalidParameterException import InvalidParameterException


class UsersRepository:

    def __init__(self):
        self.tokens = []

    @staticmethod
    def __create_connection() -> pymysql.Connection:
        return pymysql.connect(
            host="localhost",
            user="root",
            password="password",
            db="instapaper",
            autocommit=True
        )

    def login(self, login_inputs):
        connection = self.__create_connection()
        email = login_inputs["email"]
        password = login_inputs["password"]
        try:
            cursor = connection.cursor()
            request = f"SELECT password FROM Authentication WHERE email = '{email}';"
            cursor.execute(request)
            entry = cursor.fetchone()
            if entry is None:
                raise InvalidParameterException("email invalid")
            hashed_password = entry[0]
            if sha256_crypt.verify(password, hashed_password):
                username = self.get_username_by_email(email)
                return {
                    "token_id": str(self.create_token(username)),
                    "username": username
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

    def create_user(self, signup_input):
        connection = self.__create_connection()
        username = signup_input["username"]
        email = signup_input['email']
        first_name = signup_input['first_name']
        last_name = signup_input['last_name']
        bio = signup_input['bio']
        hashed_password = sha256_crypt.hash(signup_input['password'])
        try:
            cursor = connection.cursor()
            request = f"INSERT INTO Users (username, email, first_name, last_name, bio) VALUES ('{username}', " \
                      f"'{email}', '{first_name}', '{last_name}', '{bio}');"
            cursor.execute(request)
            request = f"INSERT INTO Authentication (email, password) VALUES ('{email}', '{hashed_password}');"
            cursor.execute(request)
            return {
                "token_id": str(self.create_token(username)),
                "username": username
            }
        finally:
            connection.close()

    def is_username_already_exists(self, username):
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Users WHERE username = '{username}';"
            cursor.execute(request)
            return cursor.fetchone() is not None
        finally:
            connection.close()

    def is_email_already_exists(self, email):
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Users WHERE email = '{email}';"
            cursor.execute(request)
            return cursor.fetchone() is not None
        finally:
            connection.close()

    def is_token_valid(self, token_id):
        token_is_valid = False
        for stocked_token in self.tokens:
            if stocked_token["token_expire_time"] < datetime.datetime.now():
                self.tokens.remove(stocked_token)
                continue
            if stocked_token["token_id"] == UUID(token_id):
                token_index = self.tokens.index(stocked_token)
                self.update_token(token_index)
                token_is_valid = True
        return token_is_valid

    def update_token(self, token_index):
        self.tokens[token_index]["token_expire_time"] = datetime.datetime.now() + datetime.timedelta(days=1)

    def logout(self, token_id):
        for stocked_token in self.tokens:
            if stocked_token["token_id"] == UUID(token_id):
                self.tokens.remove(stocked_token)
                break

    def get_user_by_token(self, token_id):
        for stocked_token in self.tokens:
            if stocked_token["token_id"] == UUID(token_id):
                return stocked_token["username"]
        return None

    def search_user(self, query: str):
        connection = self.__create_connection()
        users = []
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Users WHERE username LIKE '%{query}%' OR email LIKE '%{query}%@%';"
            cursor.execute(request)
            columns = [key[0] for key in cursor.description]
            users = [dict(zip(columns, user)) for user in cursor.fetchall()]
        finally:
            connection.close()
        return users
