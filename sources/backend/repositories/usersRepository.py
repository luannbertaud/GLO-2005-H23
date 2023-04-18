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
        """
        Méthode permettant d'enregistrer un utilisateur comme connecté pour ce serveur.
        Les données nécessaires dans le payload sont : 'email' et 'password'.
        :param login_inputs: Json contenant les différentes informations nécessaires à la connexion.
        :return: Un token de connexion valide pour l'utilisateur ou une InvalidParameterException.
        """
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
        """
        Méthode permettant de créer un token valide pour le nom d'utilisateur passé en paramètre.
        Le token est aussi stocké dans la mémoire de ce serveur.
        :param username: Nom d'utilisateur pour qui générer un token.
        :return: Un token de session valide pendant 24h.
        """
        token_id = uuid4()
        token_creation_time = datetime.datetime.now()
        token_expire_time = datetime.datetime.now() + datetime.timedelta(days=1)
        new_token = {"token_id": token_id, "token_creation_time": token_creation_time,
                     "token_expire_time": token_expire_time, "username": username}
        self.tokens.append(new_token)
        return new_token["token_id"]

    def get_username_by_email(self, email):
        """
        Méthode permettant d'obtenir le username d'un utilisateur à partir de son email.
        :return: Le nom d'utilisateur correspondant à l'email en paramètre.
        """
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT username FROM Users WHERE LOWER(email) = LOWER('{email}');"
            cursor.execute(request)
            return cursor.fetchone()[0]
        finally:
            connection.close()

    def create_user(self, signup_input):
        """
        Méthode permettant de créer un commentaire dans la base de données suivant les valeurs du payload passées en
        paramètre. Les valeurs du payload sont toutes nécessaires : 'username', 'email', 'first_name', 'last_name',
        'bio' et 'password'.
        :return: Un token de connexion valide pour l'utilisateur nouvellement créé.
        """
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

    def delete_user(self, token_id, username):
        """
        Supprime un utilisateur dans la base de données.
        :param username: Nom d'utilisateur avec lequel identifier l'utilisateur à supprimer.
        :return: True si le commentaire a été supprimé, False sinon.
        """
        connection = self.__create_connection()
        for stocked_token in self.tokens:
            if stocked_token["token_id"] == UUID(token_id):
                try:
                    cursor = connection.cursor()
                    request = f"DELETE FROM Users WHERE LOWER(username) = LOWER('{username}');"
                    affected_columns = cursor.execute(request)
                finally:
                    connection.close()
                return affected_columns != 0

    def is_username_already_exists(self, username):
        """
        Méthode permettant de savoir si un nom d'utilisateur est déjà utilisé.
        :param username: Nom d'utilisateur recherché.
        :return: Un boolean signifiant si oui ou non le nom d'utilisateur existe déjà.
        """
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Users WHERE LOWER(username) = LOWER('{username}');"
            cursor.execute(request)
            return cursor.fetchone() is not None
        finally:
            connection.close()

    def is_email_already_exists(self, email):
        """
        Méthode permettant de savoir si un email est déjà utilisé.
        :param email: Email recherché.
        :return: Un boolean signifiant si oui ou non l'email existe déjà.
        """
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Users WHERE LOWER(email) = LOWER('{email}');"
            cursor.execute(request)
            return cursor.fetchone() is not None
        finally:
            connection.close()

    def is_token_valid(self, token_id):
        """
        Méthode permettant de vérifier si un token est valide. (Considéré comme connecté par ce serveur).
        :param token_id: L'id du token devant est vérifié.
        :return: Un boolean signifiant la validité du token.
        """
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
        """
        Méthode permettant de rafraichir le délai d'expiration d'un token.
        :param token_index: Index du token ciblé par le rafraîchissent.
        """
        self.tokens[token_index]["token_expire_time"] = datetime.datetime.now() + datetime.timedelta(days=1)

    def logout(self, token_id):
        """
        Méthode permettant de supprimer un token de session enregistré sur ce serveur.
        :param token_id: Id du token à supprimer.
        """
        for stocked_token in self.tokens:
            if stocked_token["token_id"] == UUID(token_id):
                self.tokens.remove(stocked_token)
                break

    def get_user_by_token(self, token_id):
        """
        Méthode permettant d'obtenir le nom d'utilisateur en relation avec un token.
        :param token_id: Identifiant du token appartenant à l'utilisateur recherché.
        :return: Le nom d'utilisateur correspondant si trouvé, None sinon.
        """
        for stocked_token in self.tokens:
            if stocked_token["token_id"] == UUID(token_id):
                return stocked_token["username"]
        return None

    def get_user_info_by_username(self, username):
        """
        Méthode retournant toutes les informations stockées en base de données sur un utilisateur.
        :param username: Nom d'utilisateur pour lequel rechercher les autres données.
        :return: Json contenant toutes les informations sur l'utilisateur recherché.
        """
        connection = self.__create_connection()
        user = None
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Users WHERE LOWER(username) = LOWER('{username}');"
            cursor.execute(request)
            columns = [key[0] for key in cursor.description]
            u_raw = cursor.fetchone()
            if u_raw is not None:
                user = dict(zip(columns, u_raw))
        finally:
            connection.close()
        return user

    def delete_user(self, token_id, username):
        """
        Supprime un utilisateur dans la base de données.
        :param username: Nom d'utilisateur avec lequel identifier l'utilisateur à supprimer.
        :return: True si le commentaire a été supprimé, False sinon.
        """
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"DELETE FROM Users WHERE LOWER(username) = LOWER('{username}');"
            self.logout(token_id)
            return cursor.execute(request) != 0
        finally:
            connection.close()

    def search_user(self, query: str):
        """
        Méthode permettant de rechercher des utilisateurs suivant le contenu de leurs noms d'utilisateur.
        :param query: Chaine de caractères partielle devant être contenu dans les noms d'utilisateurs.
        :return: Une liste des utilisateurs correspondant à la recherche.
        """
        connection = self.__create_connection()
        users = []
        try:
            cursor = connection.cursor()
            request = f"SELECT * FROM Users WHERE username LIKE '%{query}%';"
            cursor.execute(request)
            columns = [key[0] for key in cursor.description]
            users = [dict(zip(columns, user)) for user in cursor.fetchall()]
        finally:
            connection.close()
        return users

    def count_followers(self, username):
        """
        Méthode permettant d'obtenir le nombre de personnes suivant un certain utilisateur.
        :param username: Nom d'utilisateur pour lequel compter les followers.
        :return: Le nombre de personnes suivant l'utilisateur ciblé.
        """
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT COUNT(id) FROM Follows WHERE LOWER(followed) = LOWER('{username}');"
            cursor.execute(request)
            count = cursor.fetchone()
            if count is None or len(count) <= 0:
                return 0
            return count[0]
        finally:
            connection.close()

    def count_following(self, username):
        """
        Méthode permettant d'obtenir le nombre de personnes étant suivis par un certain utilisateur.
        :param username: Nom d'utilisateur pour lequel compter les followings.
        :return: Le nombre de personnes étant suivis par l'utilisateur ciblé.
        """
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT COUNT(id) FROM Follows WHERE LOWER(follower) = LOWER('{username}');"
            cursor.execute(request)
            count = cursor.fetchone()
            if count is None or len(count) <= 0:
                return 0
            return count[0]
        finally:
            connection.close()
