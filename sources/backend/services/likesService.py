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
        if self.user_repository.get_user_by_token(token_id) == input_like["author"]:
            return self.like_repository.like(input_like)
        else:
            return 'Unauthorized', 401

    def unlike(self, token_id, input_like):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        if self.user_repository.get_user_by_token(token_id) == input_like["author"]:
            return self.like_repository.unlike(input_like)
        else:
            return 'Unauthorized', 401
