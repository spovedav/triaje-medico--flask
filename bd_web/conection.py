
#cmd > pip install pymySQL 

import pymysql.cursors

class conexion():
    #connection = ''
    try:
        global conn
        def conn_open(self):
            self.connection = pymysql.connect(host='localhost',
                                            user='root',
                                            password='',
                                            db='bd_empresarial',
                                            charset='utf8mb4',
                                            cursorclass=pymysql.cursors.DictCursor
                                            )
            return self.connection
    except:
        pass
        

conexion=conexion()
conn=conexion.conn_open()


