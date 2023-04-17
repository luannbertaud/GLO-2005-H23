from repositories.usersRepository import UsersRepository
from repositories.notificationsRepository import NotificationsRepository

from exceptions.MissingParameterException import MissingParameterException


class NotificationsService:

    def __init__(self, user_repository: UsersRepository, notif_repository: NotificationsRepository):
        self.user_repository = user_repository
        self.notif_repository = notif_repository

    def get_last_notifs(self, token_id):
        """
        Méthode permettant de sélectionner une liste de Notification pour un utilisateur
         dans un ordre chronologique inverse.
        :param token_id: Le token de l'utilisateur faisant la requête.
        :return: Une liste des Notifications concernant l'utilisateur.
        """
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        res = self.notif_repository.get_last_notifs(self.user_repository.get_user_by_token(token_id))
        return res
    
    def set_read_notifs(self, token_id):
        """
        Méthode permettant d'indiquer les notifications d'un utilisateur comme lues.
        :param token_id: Le token de l'utilisateur faisant la requête.
        :return: True si certains états de Notifications ont été modifiés, False sinon.
        """
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        return self.notif_repository.set_notifs_read(self.user_repository.get_user_by_token(token_id))
