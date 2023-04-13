import time

from exceptions.MissingParameterException import MissingParameterException
from repositories.commentsRepository import CommentsRepository
from repositories.postsRepository import PostsRepository
from repositories.usersRepository import UsersRepository


class PostsService:

    def __init__(self, user_repository: UsersRepository, posts_repository: PostsRepository,
                 comments_repository: CommentsRepository):
        self.user_repository = user_repository
        self.posts_repository = posts_repository
        self.comments_repository = comments_repository

    def get_latest_posts(self, token_id, page: int, page_size: int):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        query_res = self.posts_repository.get_latest_posts(page, page_size)
        for post in query_res:
            post["timestamp"] = time.mktime(post["timestamp"].timetuple())
            post["comments"] = self.comments_repository.get_comments_of_post(post["id"])
            for com in post["comments"]:
                com["timestamp"] = time.mktime(com["timestamp"].timetuple())
        return query_res
