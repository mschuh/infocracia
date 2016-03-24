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
    'Class used to store and transfer the data of a term of Federal Deputy, it has the same fields as out FDT table'
    def __init__(self, id, personId, state, initialDate, finalDate=None):
        self.id = id
        self.personId = personId
        self.state = state
        self.initialDate = initialDate
        self.finalDate = finalDate
