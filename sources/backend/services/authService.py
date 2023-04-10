import re

from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.MissingParameterException import MissingParameterException


class AuthService:

    def __init__(self, user_repository):
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
