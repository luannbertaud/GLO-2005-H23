import re

from sources.backend.exceptions.InvalidParameterException import InvalidParameterException
from sources.backend.exceptions.MissingParameterException import MissingParameterException
from sources.backend.repositories.usersRepository import UsersRepository


class AuthService:

    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    def login(self, login_inputs):
        self.__verify_login_inputs(login_inputs)
        return self.user_repository.login(login_inputs)

    @staticmethod
    def __verify_login_inputs(login_inputs):
        if "email" not in login_inputs or "password" not in login_inputs:
            raise MissingParameterException('email or password is missing for login')
        if login_inputs['email'] == '' or login_inputs['password'] == '':
            raise InvalidParameterException('Invalid parameter')
        if not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', login_inputs['email']):
            raise InvalidParameterException('Invalid email')
    
    def is_token_valid(self, token_id):
        if token_id == "":
            raise InvalidParameterException("token_id is empty")
        return self.user_repository.is_token_valid(token_id)

    def logout(self, token_id):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        self.user_repository.logout(token_id)