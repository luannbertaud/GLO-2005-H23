import os

import pymysql
from os import listdir

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="@Riane24",
    db="GLO_2005_H23",
    autocommit=True
)

cursor = connection.cursor()

if __name__ == '__main__':
    test = open("./database/users.sql", 'r')