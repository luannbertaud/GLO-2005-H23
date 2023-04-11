import pymysql
from uuid import uuid4
from passlib.hash import sha256_crypt
import datetime

from sources.backend.exceptions.InvalidParameterException import InvalidParameterException
from sources.backend.exceptions.MissingParameterException import MissingParameterException

class Users:

    def __int__(self):
        print("1")
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
        self.__verify_signup_input(signup_input)
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
            request = f"INSERT INTO Auth (email, password) VALUES ('{email}', '{hashed_password}');"
            cursor.execute(request)
            return cursor.lastrowid
        finally:
            connection.close()

    def __verify_signup_input(self, signup_input):
        if 'email' not in signup_input or 'username' not in signup_input or 'first_name' not in signup_input \
                or 'last_name' not in signup_input or 'bio' not in signup_input or 'password' not in signup_input:
            raise MissingParameterException('One or more parameters are missing')

        if signup_input['email'] == '' or signup_input['username'] == '' or signup_input['first_name'] == '' \
                or signup_input['last_name'] == '' or signup_input['bio'] == '' or signup_input['password'] == '':
            raise InvalidParameterException('Invalid parameter')

        if not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', signup_input['email']):
            raise InvalidParameterException('Invalid email')

        if self.user_repository.username_exists(signup_input['username']):
            raise InvalidParameterException('Username already exists')

        if self.user_repository.email_exists(signup_input['email']):
            raise InvalidParameterException('Email already exists')
