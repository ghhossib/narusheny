# файл для подключения к бд
from peewee import *
mysql_db = MySQLDatabase('StaN1234_naruch_ne',
                         user='StaN1234_mount',
                         password='111111',
                         host='10.11.13.118',
                         port=3306)

if __name__ == "__main__":
    print(mysql_db.connection())

