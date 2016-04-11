import xml.etree.ElementTree as ElementTree
import urllib2

from db_connection import *
from model import *

print('Downloading general deputies info...')
deputiesReader = urllib2.urlopen('http://www.camara.gov.br/SitCamaraWS/Deputados.asmx/ObterDeputados')
deputiesXml = deputiesReader.read()
print('Parsing deputies\' information...')
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
    if not profession.strip():
        #Verifies if the profession is empty by removing all useless characters and checking if the string is empty
        profession = None

    term = deputyDataTree.find('periodosExercicio').find('periodoExercicio')

    initialDateArray = term.findtext('dataInicio').split('/')
    #format form dd/mm/yyyy to yyyy-mm-dd
    initialDate = '-'.join(reversed(initialDateArray))

    finalDateString = term.findtext('dataFim')
    finalDate = ''
    if not finalDateString.strip():
        #Verifies if the finalDate is empty by removing all useless characters and checking if the string is empty
        finalDate = None
    else:
        finalDate = '-'.join(reversed(finalDateString.split('/')))
        #format form dd/mm/yyyy to yyyy-mm-dd

    birthDateArray = deputyDataTree.findtext('dataNascimento').split('/')
    birthDate = '-'.join(reversed(birthDateArray))
    #format form dd/mm/yyyy to yyyy-mm-dd

    print('Inserting info from Deputy ' + politicalName + ' into database...')
    newPerson = PersonDTO(name, politicalName, birthDate, gender, email, photoUrl, profession)
    personId = PersonDAO.insertPersonOnDB(newPerson)

    newFederalDeputyTerm = FederalDeputyTermDTO(chamberId, personId, state, initialDate, finalDate)
    FederalDeputyTermDAO.insertTermOnDB(newFederalDeputyTerm)
