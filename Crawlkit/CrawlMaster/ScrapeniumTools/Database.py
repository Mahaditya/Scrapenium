import mysql.connector
import datetime
import time

class Database: 
    def __init__(self,database,host,user='root',password='password'):
        self.database=database
        self.host=host
        self.user=user
        self.password=password
    def export_list(self,tableName,feilds,data):
        conn = mysql.connector.connect(
        user=self.user, 
        password=self.password, 
        host=self.host, 
        database=self.database)
        cursor = conn.cursor()
        ts = time.time()
        number_of_values = len(data)
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        data.append(timestamp)
        values="("+"%s,"*number_of_values+"%s)"
        insert_stmt = (
        "INSERT INTO %s%s,created_at)" % (tableName,feilds[:-1])+
        " VALUES %s" % values
        )
        data = tuple(value for value in data)
        try:
            cursor.execute(insert_stmt, data)
            conn.commit()
            print("Data inserted")
        except:
            conn.rollback()
            conn.close()
            print("failed")   


