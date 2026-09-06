import pymssql
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.sql import text as sql_text

class DBHelper():

    def __init__(self):
        self.db_host = r''
        self.db_name = r''
        self.db_user = r'' 
        self.db_password = r''

######################################################
##                   data connection                ##
######################################################
    def get_engine(self):
        str_format = 'mssql+pymssql://{0}:{1}@{2}/{3}?charset=utf8'
        connection_str = str_format.format(self.db_user,self.db_password,self.db_host,self.db_name)
        engine = create_engine(connection_str,echo=False)
        return engine

######################################################
##                common SQL APIs                   ##
######################################################
    def write_data(self,df,destination,if_exists='append',schema='dbo'):
        engine = self.get_engine()
        df.to_sql(destination, con=engine, if_exists=if_exists,index = False, schema=schema, method='multi', chunksize=100)

    def read_data(self,sql):
        engine = self.get_engine()
        df = pd.read_sql(sql, con=engine)
        return df

    def exec_sql(self,sql):
        engine = self.get_engine()
        with engine.connect() as con:
            with con.begin(): 
                con.execute(sql_text(sql).execution_options(autocommit=True))