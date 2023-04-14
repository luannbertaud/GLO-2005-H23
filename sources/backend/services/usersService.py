import re
from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.MissingParameterException import MissingParameterException
from repositories.usersRepository import UsersRepository


class UsersService:

    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    def create_user(self, signup_input):
        self.__verify_signup_input(signup_input)
        return self.user_repository.create_user(signup_input)

    def __verify_signup_input(self, signup_input):
        if 'email' not in signup_input or 'username' not in signup_input or 'first_name' not in signup_input \
                or 'last_name' not in signup_input or 'bio' not in signup_input or 'password' not in signup_input:
            raise MissingParameterException('One or more parameters are missing')

        if signup_input['email'] == '' or signup_input['username'] == '' or signup_input['first_name'] == '' \
                or signup_input['last_name'] == '' or signup_input['bio'] == '' or signup_input['password'] == '':
            raise InvalidParameterException('Invalid parameter')

        if not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', signup_input['email']):
            raise InvalidParameterException('Invalid email')

        if self.user_repository.is_username_already_exists(signup_input['username']):
            raise InvalidParameterException('Username already exists')

        if self.user_repository.is_email_already_exists(signup_input['email']):
            raise InvalidParameterException('Email already exists')
