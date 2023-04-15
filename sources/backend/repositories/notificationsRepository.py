from datetime import datetime

import pymysql

from exceptions.InvalidParameterException import InvalidParameterException
from repositories.usersRepository import UsersRepository


class NotificationsRepository:

    def __init__(self, user_repository: UsersRepository):
        self.user_repository = user_repository

    @staticmethod
    def __create_connection() -> pymysql.Connection:
        return pymysql.connect(
            host="localhost",
            user="root",
            password="password",
            db="instapaper",
            autocommit=True
        )

    def get_last_notifs(self, username):
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"SELECT post_id, l.author, l.timestamp, status FROM Likes AS l, Posts AS p, (SELECT * FROM Notifications WHERE type = 'like') AS n WHERE l.id = n.id AND p.id = l.post_id AND p.author = 'OceanicOctopus';"
            """ request = f"SELECT Notifications.id, Follows.follower FROM Notifications JOIN Follows ON Notifications.type = 'follow' AND Notifications.id = Follows.id WHERE Follows.followed = 'GalacticSailor';" """
            """ request = f"SELECT n.id, n.type, n.status, CASE " \
                      f"WHEN n.type = 'like' THEN l.author WHEN n.type = 'comment' THEN c.author WHEN n.type = 'follow' THEN f.follower" \
                      f"ELSE '' END AS author_name" \
                      f"FROM Notifications n" \
                      f"LEFT JOIN Likes l ON n.id = l.id AND n.type = 'like'" \
                      f"LEFT JOIN Comments c ON n.id = c.id AND n.type = 'comment'" \
                      f"LEFT JOIN Follows f ON n.id = f.id AND n.type = 'follow'" \
                      f"WHERE f.follower = '{username}' OR l.author = '{username}' OR c.author = '{username}'" \
                      f"ORDER BY n.id DESC LIMIT 5;" """
            cursor.execute(request)
            res = cursor.fetchall()
            return res
        finally: connection.close()

