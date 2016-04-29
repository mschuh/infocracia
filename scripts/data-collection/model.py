class PersonDTO:
    'Class used to store and transfer the data of a Person on our data base, it has the same fields as our person table'
    def __init__(self, name, politicalName, birthDate, gender, email, photoUrl, profession=None):
        self.name = name
        self.politicalName = politicalName
        self.birthDate = birthDate
        self.gender = gender
        self.email = email
        self.photoUrl = photoUrl
        self.profession = profession

class FederalDeputyTermDTO:
    'Class used to store and transfer the data of a term of Federal Deputy'
    def __init__(self, id, personId, state, initialDate, finalDate=None):
        self.id = id
        self.personId = personId
        self.state = state
        self.initialDate = initialDate
        self.finalDate = finalDate

class ChamberAgencyDTO:
    'Class used to store and trasfer data of an angecy from the Deputies Chamber'
    def __init__(self, id, acronym, description, active):
        self.id = id
        self.acronym = acronym
        self.description = description
        self.active = active

class FedDeputyAgencyParticipationDTO:
    'Class used to store and trasfer the relation between a federal deputy term and an agency'
    def __init__(self, federalDeputyTermId, chamberAgencyId, role):
        self.federalDeputyTermId = federalDeputyTermId
        self.chamberAgencyId = chamberAgencyId
        self.role = role

class PartyDTO:
    'Class used to store and trasfer the data of a Party on our database, it has the same fields as our party table'
    def __init__(self, name, acronym, photoUrl):
        self.name = name
        self.acronym = acronym
        self.photoUrl = photoUrl

class FiliationDTO:
    'Class used to store and trasfer the relation between a person and a party'
    def __init__(self, initialDate, finalDate, personId, partyId):
        self.initialDate = initialDate
        self.finalDate = finalDate
        self.personId = personId
        self.partyId = partyId

class SenatorTermDTO:
    'Class used to store and trasfer the data of a term of Senator'
    def __init__(self, id, personId, state, initialDate, finalDate):
        self.id = id
        self.personId = personId
        self.state = state
        self.initialDate = initialDate
        self.finalDate = finalDate

class SenateCommissionDTO:
    'Class used to store and trasfer data of a commission from the Senate'
    def __init__(self, id, acronym, name, active):
        self.id = id
        self.acronym = acronym
        self.name = name
        self.active = active

class SenateCommissionParticipationDTO:
    'Class used to store and trasfer the relation between a senator term and a senate comission'
    def __init__(self, senatorTermId, senateCommissionId, role):
        self.senatorTermId = senatorTermId
        self.senateCommissionId = senateCommissionId
        self.role = role

class ExecutiveTermDTO:
    'Class used to store and transfer the data of a term of Federal Deputy'
    def __init__(self, personId, state, initialDate, finalDate, role):
        self.personId = personId
        self.state = state
        self.initialDate = initialDate
        self.finalDate = finalDate
        self.role = role
