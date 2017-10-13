# -*- coding: utf-8 -*-
from impala.dbapi import connect
from impala.util import as_pandas

#class HiveClient(object):
#    def __init__(self, host, user, password, database, port=10000, auth_mechanism="PLAIN"):
#        self.conn = connect(host = host,
#                            user = user,
#                            password = password,
#                            database = database,
#                            port = port,
#                            auth_mechanism = auth_mechanism)
#    
#    def query(self, sql):
#        cursor = self.conn.cursor()
#        cursor.execute(sql)
#        return cursor.fetchall()
#    
#    def close(self):
#        self.conn.close()

class HiveClient(object):
    def __init__(self, host, user, password, database, port=10000, auth_mechanism="PLAIN"):
        self.conn = connect(host = host,
                            user = user,
                            password = password,
                            database = database,
                            port = port,
                            auth_mechanism = auth_mechanism)
    
    def query(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return as_pandas(cursor)
    
    def close(self):
        self.conn.close()
