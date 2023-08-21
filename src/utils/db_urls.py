from os import getenv

from dotenv import load_dotenv


def get_mysql_url(load: bool = load_dotenv()):
    server = "mysql"
    driver = "mysqlconnector"

    params = {
        "name": getenv("DATABASE_NAME"),
        "username": getenv("DATABASE_USER"),
        "password": getenv("DATABASE_PASSWD"),
        "host": getenv("DATABASE_HOST"),
    }

    mysql_url = (
        f"{server}+{driver}://{params['username']}:"
        f"{params['password']}@{params['host']}/{params['name']}"
    )

    return mysql_url
