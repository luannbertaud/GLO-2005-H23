from datetime import datetime

import json
import pymysql

from exceptions.InvalidParameterException import InvalidParameterException
from repositories.usersRepository import UsersRepository

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        return json.JSONEncoder.default(self, obj)

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
            request = "SELECT follower, followed, timestamp, status, type FROM Follows AS f, (SELECT * FROM Notifications WHERE type = 'follow') AS n WHERE f.id = n.id AND followed = '{username}';"
            cursor.execute(request)
            resFollow = cursor.fetchall()
            request = "SELECT post_id, c.author, c.timestamp, status, type FROM Comments as c, Posts as p, (SELECT * FROM Notifications WHERE type = 'comment') as n WHERE c.id = n.id AND p.id = c.post_id AND p.author = '{username}';"
            cursor.execute(request)
            resComment = cursor.fetchall()
            request = "SELECT post_id, l.author, l.timestamp, status, type FROM Likes as l, Posts as p, (SELECT * FROM Notifications WHERE type = 'like') as n WHERE l.id = n.id AND p.id = l.post_id AND p.author = '{username}';"
            cursor.execute(request)
            resLike = cursor.fetchall() 
            res = resFollow + resComment + resLike
            print(res)
            return json.dumps(res, cls=DateTimeEncoder)
        finally: connection.close()

    def set_notifs_read(self, username):
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"UPDATE Notifications SET status = 'read' WHERE type = 'follow' AND id IN (SELECT id FROM Follows WHERE followed = '{username}');"
            res = cursor.execute(request) != 0
            request = f"UPDATE Notifications n INNER JOIN Comments c ON n.id = c.id INNER JOIN Posts p ON c.post_id = p.id SET n.status = 'read' WHERE n.type = 'comment' AND c.author != '{username}' AND p.author = '{username}';"
            res = cursor.execute(request) != 0
            request = f"UPDATE Notifications AS n, Likes AS l, Posts AS p SET n.status = 'read' WHERE n.id = l.id AND l.post_id = p.id AND p.author = '{username}' AND n.type = 'like';"
            res = cursor.execute(request) != 0
            return res
        finally: connection.close()

