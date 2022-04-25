from exts.ext import dbs
from datetime import datetime
from . import BaseModel

class NewsModel(BaseModel):
    __tablename='news'
    title = dbs.Column(dbs.String(20),nullable=False)
    content = dbs.Column(dbs.Text,nullable=False)