from sources.backend.repositories.usersRepository import UsersRepository
from sources.backend.repositories.postsRepository import PostsRepository
from sources.backend.exceptions.MissingParameterException import MissingParameterException



class PostsService:

    def __init__(self, user_repository: UsersRepository, post_repository: PostsRepository):
        self.user_repository = user_repository
        self.post_repository = post_repository

    def post(self, token_id, input_post):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        if self.user_repository.get_user_by_token(token_id) == input_post["author"]:
            return self.post_repository.post(input_post)
        else:
            return 'Unauthorized', 401

    def delete_post(self, token_id, input_post):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        if self.user_repository.get_user_by_token(token_id) == input_post["author"]:
            return self.post_repository.delete_post(input_post)
        else:
            return 'Unauthorized', 401
