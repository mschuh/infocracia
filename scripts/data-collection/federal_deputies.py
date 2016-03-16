import xml.etree.ElementTree as ElementTree
import urllib2

from db_connection import DbConnection

class PersonDTO:
    'Class used to store and transfer the data of a Person on our data base, it has the same fields as our person table'
    def __init__(self, name, politicalName, birthDate, gender, email, photoUrl, profession=None):
        self.name = name
        self.politicalName = politicalName
        self.birthDate = birthDate
        self.gender = gender
        self.profession = profession
        self.email = email
        self.photoUrl = photoUrl

class PersonDAO:
    'Data access object of for person, include the methods for inserting and retrieving a person from the data base'

class FederalDeputyTermDTO:
    'Class used to store and transfer the data of a term of Federal Deputy, it has the same fields as out FDT table'
    def __init__(self, id, personId, state, initialDate, finalDate=None):
        self.id = id
        self.personId = personId
        self.state = state
        self.initialDate = initialDate
        self.finalDate = finalDate

print('Downloading general deputies info...')
deputiesReader = urllib2.urlopen('http://www.camara.gov.br/SitCamaraWS/Deputados.asmx/ObterDeputados')
deputiesXml = deputiesReader.read()
print('Parsing general deputies file...')
deputiesDataTree = ElementTree.fromstring(deputiesXml)

i = 0
for deputy in deputiesDataTree:
    chamberId = deputy.findtext('ideCadastro')

    name = deputy.findtext('nome')
    politicalName = deputy.findtext('nomeParlamentar')
    gender = deputy.findtext('sexo')
    email = deputy.findtext('email')
    photoUrl = deputy.findtext('urlFoto')
    state = deputy.findtext('uf')

    i += 1
    print('Downloading detailed info from Deputy ' + politicalName + ' (' + str(i) + '/' +
                                    str(len(deputiesDataTree)) + ')')
    deputyReader = urllib2.urlopen('http://www.camara.gov.br/SitCamaraWS/Deputados.asmx/ObterDetalhesDeputado' +
                                    '?ideCadastro=' + chamberId + '&numLegislatura=55')
    deputyXml = deputyReader.read()
    deputyDataTree = ElementTree.fromstring(deputyXml).find('Deputado')

    profession = deputyDataTree.findtext('nomeProfissao')
