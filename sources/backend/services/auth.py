from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.MissingParameterException import MissingParameterException


class Auth:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def login(self, login_inputs):
        self.__verify_login_inputs(login_inputs)
        return self.user_repository.login(login_inputs)

    @staticmethod
    def __verify_login_inputs():
        if "email" not in user_credential or "password" not in user_credential:
            raise MissingParameterException('email or password is missing for login')
        if user_credential['email'] == '' or user_credential['password'] == '':
            raise InvalidParameterException('Invalid parameter')
        if not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', user_credential['email']):
            raise InvalidParameterException('Invalid email')
