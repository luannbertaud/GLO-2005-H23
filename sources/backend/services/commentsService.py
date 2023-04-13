from repositories.usersRepository import UsersRepository


class CommentsService:

    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository
