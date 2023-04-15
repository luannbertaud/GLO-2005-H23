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
            request = f"SELECT n.id, n.type, n.status, CASE WHEN n.type = 'like' THEN l.author WHEN n.type = 'comment' THEN c.author WHEN n.type = 'follow' THEN f.follower ELSE '' END AS author_name FROM Notifications n LEFT JOIN Likes l ON n.id = l.id AND n.type = 'like' LEFT JOIN Comments c ON n.id = c.id AND n.type = 'comment' LEFT JOIN Follows f ON n.id = f.id AND n.type = 'follow' WHERE f.follower = 'CelestialCentipede' OR l.author = 'CelestialCentipede' OR c.author = 'CelestialCentipede' ORDER BY n.id DESC LIMIT 5;"
            cursor.execute(request)
            res = cursor.fetchall()
            return json.dumps(res, cls=DateTimeEncoder)
        finally: connection.close()

    def set_notifs_read(self, username):
        connection = self.__create_connection()
        try:
            cursor = connection.cursor()
            request = f"UPDATE Notifications SET status = 'read' WHERE id IN (SELECT id FROM (SELECT id FROM Likes WHERE author = 'CelestialCentipede' UNION ALL SELECT id FROM Comments WHERE author = 'CelestialCentipede' UNION ALL SELECT id FROM Follows WHERE follower = 'CelestialCentipede') AS sub_query);"
            return cursor.execute(request) != 0
        finally: connection.close()

