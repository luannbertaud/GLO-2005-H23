from repositories.usersRepository import UsersRepository
from repositories.likesRepository import LikesRepository

from exceptions.MissingParameterException import MissingParameterException


class LikesService:

    def __init__(self, user_repository: UsersRepository, like_repository: LikesRepository):
        self.user_repository = user_repository
        self.like_repository = like_repository

    def like(self, token_id, input_like):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        self.like_repository.like(self.user_repository.get_user_by_token(token_id), input_like["post_id"])
        return "Successfully liked", 200

    def unlike(self, token_id, input_like):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        self.like_repository.unlike(self.user_repository.get_user_by_token(token_id), input_like["post_id"])
        return "Successfully unliked", 200
