import re

from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.MissingParameterException import MissingParameterException
from repositories.usersRepository import UsersRepository


class AuthService:

    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    def login(self, login_inputs):
        """
        Méthode permettant l'obtention d'un token d'authentification valide en échange d'un
        payload contenant un champ 'email' et un champ 'password'.
        :param login_inputs: Le Payload contenant les champs nécessaires à la validation de la connection.
        :return: Le token d'authentification ou une InvalidParameterException.
        """
        self.__verify_login_inputs(login_inputs)
        return self.user_repository.login(login_inputs)

    @staticmethod
    def __verify_login_inputs(login_inputs):
        """
        Méthode permettant la validation des données concernant la connexion à un de compte.
        :param login_inputs: Json contenant les données nécessaires à la connexion à un compte.
        :return: Ne retourne rien, mais les exceptions MissingParameterException et InvalidParameterException
        peuvent apparaitre suivant les erreurs contenues dans les données d'entrée.
        """
        if "email" not in login_inputs or "password" not in login_inputs:
            raise MissingParameterException('email or password is missing for login')
        if login_inputs['email'] == '' or login_inputs['password'] == '':
            raise InvalidParameterException('Invalid parameter')
        if not re.fullmatch(r'[^@]+@[^@]+\.[^@]+', login_inputs['email']):
            raise InvalidParameterException('Invalid email')
    
    def is_token_valid(self, token_id):
        """
        Méthode permettant la vérification de la validité d'un token.
        :param token_id: L'id du token à vérifier.
        :return: Un boolean correspondant à la validité du token.
        """
        if token_id == "":
            raise InvalidParameterException("token_id is empty")
        return self.user_repository.is_token_valid(token_id)

    def logout(self, token_id):
        """
        Méthode qui supprime le token enregistré pour un certain utilisateur,
         ce qui le supprime des données du serveur.
        """
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        self.user_repository.logout(token_id)

    def get_user_by_token(self, token_id):
        """
        Méthode retournant le nom d'un utilisateur suivant un ID de token si l'utilisateur est connecté.
        :param token_id: L'id du token appartenant à l'utilisateur.
        :return: Le nom d'utilisateur de l'utilisateur si trouvé, None sinon.
        """
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        return self.user_repository.get_user_by_token(token_id)
