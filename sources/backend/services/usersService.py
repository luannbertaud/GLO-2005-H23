import re

from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.MissingParameterException import MissingParameterException
from repositories.likesRepository import LikesRepository
from repositories.usersRepository import UsersRepository


class UsersService:

    def __init__(self, user_repository: UsersRepository, like_repository: LikesRepository):
        self.user_repository = user_repository
        self.like_repository = like_repository

    def create_user(self, signup_input):
        self.__verify_signup_input(signup_input)
        return self.user_repository.create_user(signup_input)

    def delete_user(self, token_id, username):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        elif self.user_repository.is_username_already_exists(username):
            self.user_repository.delete_user(token_id, username)
            return "Successfully deleted", 200
        else:
            raise InvalidParameterException('User does not exist')

    def get_user_info_by_username(self, username):
        if self.user_repository.is_username_already_exists(username):
            user = self.user_repository.get_user_info_by_username(username)
            user['following'] = self.user_repository.count_following(username)
            user['followers'] = self.user_repository.count_followers(username)
            user['likes'] = self.like_repository.count_likes_for_user(username)
            return user
        else:
            raise InvalidParameterException('User does not exist')

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
