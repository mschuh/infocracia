import mysql.connector
from model import *

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
    'Data access object for federal deputy term, include the methods for inserting and retrieving a terms from the DB'
    @staticmethod
    def insertTermOnDB(federalDeputyTermDTO):
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

    @staticmethod
    def findTermById(id):
        #returns a FederalDeputyTermDTO containing the data corresponding to the passed id
        dbConnection = DbConnection()
        cnx = dbConnection.connection
        cursor = cnx.cursor()

        selectTermRequest = ("SELECT * FROM federal_deputy_term WHERE id=" + str(id))

        cursor.execute(selectTermRequest)
        termRow = cursor.fetchone()

        return FederalDeputyTermDTO(termRow[0], termRow[1], termRow[2], termRow[3], termRow[4])

class ChamberAgencyDAO:
    'Data access object for chamber agency, include the methods for inserting and retrieving an agency from the DB'
    @staticmethod
    def insertAgencyOnDB(chamberAgencyDTO):
        #insert a federal deputy term on the database
        dbConnection = DbConnection()
        cnx = dbConnection.connection
        cursor = cnx.cursor()

        addAgencyRequest = ("INSERT INTO chamber_agency "
                          "(id, acronym, description, active) "
                          "VALUES (%(id)s, %(acronym)s, %(description)s, %(active)s)")

        cursor.execute(addAgencyRequest, chamberAgencyDTO.__dict__)
        cnx.commit()
        cnx.close()

    @staticmethod
    def findAgencyById(id):
        #returns a FederalDeputyTermDTO containing the data corresponding to the passed id
        dbConnection = DbConnection()
        cnx = dbConnection.connection
        cursor = cnx.cursor()

        selectTermRequest = ("SELECT * FROM chamber_agency WHERE id=" + str(id))

        cursor.execute(selectTermRequest)
        termRow = cursor.fetchone()

        return ChamberAgencyDTO(termRow[0], termRow[1], termRow[2], termRow[3])

class FedDeputyAgencyParticipationDAO:
    """
    Data access object for deputy participation on agencies, include the methods for inserting and retrieving a
    participation from the data base'
    """
    @staticmethod
    def insertParticipationOnDB(fedDeputyAgencyParticipationDTO):
        #insert a federal deputy term on the database
        dbConnection = DbConnection()
        cnx = dbConnection.connection
        cursor = cnx.cursor()

        addAgencyRequest = ("INSERT INTO federal_deputy_term_agency_participation "
                          "(federal_deputy_term_id, agency_id, role) "
                          "VALUES (%(federalDeputyTermId)s, %(chamberAgencyId)s, %(role)s)")

        cursor.execute(addAgencyRequest, fedDeputyAgencyParticipationDTO.__dict__)
        cnx.commit()
        cnx.close()
