import re
from sources.backend.exceptions.InvalidParameterException import InvalidParameterException
from sources.backend.exceptions.MissingParameterException import MissingParameterException
from sources.backend.repositories.userRepository import UserRepository


class UsersService:

    def __int__(self, user_repository: UserRepository):
        print("test")
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

        if self.user_repository.username_exists(signup_input['username']):
            raise InvalidParameterException('Username already exists')

        if self.user_repository.email_exists(signup_input['email']):
            raise InvalidParameterException('Email already exists')
