import time

from exceptions.MissingParameterException import MissingParameterException
from repositories.commentsRepository import CommentsRepository
from repositories.likesRepository import LikesRepository
from repositories.postsRepository import PostsRepository
from repositories.usersRepository import UsersRepository


class PostsService:

    def __init__(self, user_repository: UsersRepository, posts_repository: PostsRepository,
                 comments_repository: CommentsRepository, likes_repository: LikesRepository):
        self.user_repository = user_repository
        self.posts_repository = posts_repository
        self.comments_repository = comments_repository
        self.likes_repository = likes_repository

    def get_latest_posts(self, token_id, page: int, page_size: int):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        query_res = self.posts_repository.get_latest_posts(page, page_size)
        for post in query_res:
            post["timestamp"] = time.mktime(post["timestamp"].timetuple())
            post["comments"] = self.comments_repository.get_comments_of_post(post["id"])
            post["likes"] = self.likes_repository.count_likes_of_post(post["id"])
            post["user_like"] = self.likes_repository.is_like_already_exists(
                self.user_repository.get_user_by_token(token_id), post["id"])
            for com in post["comments"]:
                com["timestamp"] = time.mktime(com["timestamp"].timetuple())
        return query_res

    def post(self, token_id, input_post):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        if self.user_repository.get_user_by_token(token_id) == input_post["author"]:
            return self.posts_repository.post(input_post)
        else:
            return 'Unauthorized', 401

    def delete_post(self, token_id, input_post):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        if self.user_repository.get_user_by_token(token_id) == input_post["author"]:
            return self.posts_repository.delete_post(input_post)
        else:
            return 'Unauthorized', 401
