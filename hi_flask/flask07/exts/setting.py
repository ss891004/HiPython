import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_db_uri(dbinfo):

    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or ""
    port = dbinfo.get("PORT") or ""
    name = dbinfo.get("NAME") or ""

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:

    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):

    DEBUG = True

    dbinfo = {

        "ENGINE": "mysql",
        "DRIVER": "mysqlconnector",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "NAME": "flask07"

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)



envs = {
    "develop": DevelopConfig
}