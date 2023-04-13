from exceptions.MissingParameterException import MissingParameterException
from repositories.postsRepository import PostsRepository
from repositories.usersRepository import UsersRepository

from datetime import datetime
import time


class PostsService:

    def __init__(self, user_repository: UsersRepository, posts_repository: PostsRepository):
        self.user_repository = user_repository
        self.posts_repository = posts_repository

    def get_latest_posts(self, token_id, page: int, page_size: int):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        query_res = self.posts_repository.get_latest_posts(page, page_size)
        for post in query_res:
            # d = datetime.strptime(post["timestamp"], "%Y/%m/%d %H:%M:%S")
            post["timestamp"] = time.mktime(post["timestamp"].timetuple())
        return query_res
