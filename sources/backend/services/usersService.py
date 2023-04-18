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
        """
        Méthode créant un utilisateur dans la base de données après avoir vérifié les données de création de compte.
        :param signup_input: Paylod contenant les différentes données nécessaires à la création d'un compte.
        :return: Un token de connection valide pour le compte créé.
        """
        self.__verify_signup_input(signup_input)
        return self.user_repository.create_user(signup_input)

    def delete_user(self, token_id, username):
        """
        Méthode supprimant un compte utilisatur après avoir vérifié s'il existe.
        :param token_id: Le token de l'utilisateur faisant la requête.
        :param username: Le nom de l'utilisateur à supprimer.
        :return: Un code 200 en cas de succès, une InvalidParameterException autrement.
        """
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        elif self.user_repository.is_username_already_exists(username):
            self.user_repository.delete_user(token_id, username)
            return "Successfully deleted", 200
        else:
            raise InvalidParameterException('User does not exist')

    def get_user_info_by_username(self, username):
        """
        Méthode retournant les données correspondantes à un utilisateur spécifique.
        :param username: Le nom d'utilisateur du compte sur lequel nous souhaitons obtenir des informations.
        :return: Un json contenant les informations suivantes : 'username', 'email', 'firstname', 'lastname', 'bio'
        'following', 'followers', 'likes', ou une InvalidParameterException si l'utilisateur n'existe pas.
        """
        if self.user_repository.is_username_already_exists(username):
            user = self.user_repository.get_user_info_by_username(username)
            user['following'] = self.user_repository.count_following(username)
            user['followers'] = self.user_repository.count_followers(username)
            user['likes'] = self.like_repository.count_likes_for_user(username)
            return user
        else:
            raise InvalidParameterException('User does not exist')

    def __verify_signup_input(self, signup_input):
        """
        Méthode permettant la validation des données concernant la création de compte.
        :param signup_input: Json contenant les données nécessaires à la création d'un compte.
        :return: Ne retourne rien, mais les exceptions MissingParameterException et InvalidParameterException
        peuvent apparaitre suivant les erreurs contenues dans les données d'entrée.
        """
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
