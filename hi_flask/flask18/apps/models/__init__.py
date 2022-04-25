from exts.ext import dbs
from datetime import datetime

class BaseModel(dbs.Model):
    __abstract__=True
    id = dbs.Column(dbs.Integer, primary_key=True, autoincrement =True)
    insert_time = dbs.Column(dbs.DateTime, default=datetime.now)