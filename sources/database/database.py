import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="@Riane24",
    db="GLO_2005_H23",
    autocommit=True
)

cursor=connection.cursor()
