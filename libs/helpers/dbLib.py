from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.sql import text
#from robot.api.deco import library, keyword
import config.dbvariables as dbvars

#library that allows to to connect and retieve queries from mssql
#connection data is saved in dbvariables
#@library(scope='GLOBAL', auto_keywords=True)
class DbLib:

    def __init__(self):
        self.dbdata = dbvars.db_variables()

    #@keyword
    def execute_sql(self, sql: str):
        #url = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver={}'.format(self.dbdata['username'], self.dbdata['password'], self.dbdata['server'],
        #                                                       self.dbdata['port'], self.dbdata['database'], 'SQL+Server')
        url = 'mssql+pymssql://{}:{}@{}/{}'.format(self.dbdata['username'], self.dbdata['password'], self.dbdata['server'],
                                                               self.dbdata['database'])
        #url = 'mssql+pymssql://{}:{}@{}/{}?port={}?trusted_connection=yes'.format(self.dbdata['username'], self.dbdata['password'], self.dbdata['server'],
        #                                                       self.dbdata['database'],  self.dbdata['port'])
        #some fake change4
        engine = create_engine(url)
        with engine.connect().execution_options(autocommit=True) as conn:
            query = conn.execute(text(sql))
            return pd.DataFrame(query.fetchall())