import mysql.connector

class DbConnection:
    'Class that will handle the interaction with our MySQL Database'
    def __init__(self):
        self.connection = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  port='3306',
                                  database='main')
        #TODO create verifications for the database connection catching the possible exceptions

    def __del__(self):
        self.connection.close()


class PersonDAO:
    'Data access object for person, include the methods for inserting and retrieving a person from the data base'
    @staticmethod
    def insertPersonOnDB(personDTO):
        #insert a person on the database and returns the unique id of this person on the database
        dbConnection = DbConnection()
        cnx = dbConnection.connection
        cursor = cnx.cursor()
        addPersonRequest = ("INSERT INTO person "
                            "(name, political_name, birth_date, gender, email, photo_url, profession) "
                            "VALUES (%(name)s, %(politicalName)s, %(birthDate)s, %(gender)s, %(email)s, %(photoUrl)s, %(profession)s)")
        cursor.execute(addPersonRequest, personDTO.__dict__)
        id = cursor.lastrowid
        cnx.commit()
        cnx.close()
        return id

    @staticmethod
    def findPersonOnDB():
        #returns a PersonDTO according to the search criteria
        print('Not yet implemented')


class FederalDeputyTermDAO:
    'Data access object for person, include the methods for inserting and retrieving a person from the data base'
    @staticmethod
    def inserTermOnDB(federalDeputyTermDTO):
        #insert a federal deputy term on the database
        dbConnection = DbConnection()
        cnx = dbConnection.connection
        cursor = cnx.cursor()

        addTermRequest = ("INSERT INTO federal_deputy_term "
                          "(id, person_id, state, initial_date, final_date) "
                          "VALUES (%(id)s, %(personId)s, %(state)s, %(initialDate)s, %(finalDate)s)")

        cursor.execute(addTermRequest, federalDeputyTermDTO.__dict__)
        cnx.commit()
        cnx.close()
