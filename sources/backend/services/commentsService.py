from datetime import datetime
import time

from exceptions.InvalidParameterException import InvalidParameterException
from exceptions.MissingParameterException import MissingParameterException
from repositories.commentsRepository import CommentsRepository
from repositories.usersRepository import UsersRepository


class CommentsService:

    def __init__(self, user_repository: UsersRepository, comments_repository: CommentsRepository):
        self.user_repository = user_repository
        self.comments_repository = comments_repository

    def delete(self, token_id, comment_id):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        comment = self.comments_repository.get_comment_by_id(comment_id)
        user = self.user_repository.get_user_by_token(token_id)
        if user is None or comment is None or user != comment["author"]:
            return 'Unauthorized', 401
        else:
            self.comments_repository.delete_comment(comment_id)
            return 'Success', 200

    def create(self, token_id, body):
        if token_id is None:
            raise MissingParameterException("token_id is missing")
        user = self.user_repository.get_user_by_token(token_id)
        if user is None or body["post_id"] is None or body["body"] is None:
            raise MissingParameterException("Missing parameters in [post_id, body]")
        else:
            (success, new_id) = self.comments_repository.create_comment(
                body["post_id"], user, body["body"], datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
            if not success:
                raise InvalidParameterException("Failed to create comment with provided parameters")
            return self.get_comment_by_id(new_id)

    def get_comment_by_id(self, comment_id):
        com = self.comments_repository.get_comment_by_id(comment_id)
        com["timestamp"] = time.mktime(com["timestamp"].timetuple())
        return com
