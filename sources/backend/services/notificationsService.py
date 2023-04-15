from repositories.usersRepository import UsersRepository
from repositories.notificationsRepository import NotificationsRepository

from exceptions.MissingParameterException import MissingParameterException


class NotificationsService:

    def __init__(self, user_repository: UsersRepository, notif_repository: NotificationsRepository):
        self.user_repository = user_repository
        self.notif_repository = notif_repository

    def get_last_notifs(self, token_id):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        query_res = self.notif_repository.get_last_notifs(self.user_repository.get_user_by_token(token_id))
        print(query_res)
        return query_res

