import mysql.connector
import time

class QASQL():

#    user = 'root'
#    pwd = 'autoqa'
#    host = '10.108.17.25'
#    db = 'autoqa'

    user = 'root'
    pwd = '30291912'
    host = 'localhost'
    db = 'crawler'
    conn = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
    cursor = conn.cursor()

    def Disconnect(self):
        self.conn.close()
        self.cursor.close()

    def getConf(self, conf):
        sel_sql = 'SELECT Id, Title, Name FROM conf_list WHERE Conf=\"{}\"'.format(conf)
        try:
            self.cursor.execute(sel_sql)
        except:
            print('conf sel err')
        arr_conf = []
        for item in self.cursor.fetchall():
            arr_conf.append(item)
        return arr_conf
'''
qa = QASQL()
qa.getConf('www')
'''
