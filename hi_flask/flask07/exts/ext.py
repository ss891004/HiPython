from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

dbs = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap5()



def init_ext(app):
    dbs.init_app(app)
    migrate.init_app(app, dbs)
    bootstrap.init_app(app)