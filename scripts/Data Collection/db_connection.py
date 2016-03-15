import mysql.connector

class DbConnection:
    'Class that will handle the interaction with our MySQL Database'
    def __init__(self):
        self.connection = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='main')
        #TODO create verifications for the database connection catching the possible exceptions        

    def __del__(self):
        self.connection.close()
