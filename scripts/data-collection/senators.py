import xml.etree.ElementTree as ElementTree
import urllib2

from db_connection import *
from model import *

print('Downloading general senators info...')
senatorsReader = urllib2.urlopen('http://legis.senado.leg.br/dadosabertos/senador/lista/atual')
senatorsXml = senatorsReader.read()
print('Parsing senators\' information...')
senatorsDataTree = ElementTree.fromstring(senatorsXml).find('Parlamentares')

i = 0
for senator in senatorsDataTree:
    basicData = senator.find('IdentificacaoParlamentar')

    senateId = basicData.findtext('CodigoParlamentar')
    name = basicData.findtext('NomeCompletoParlamentar')
    politicalName = basicData.findtext('NomeParlamentar')
    gender = basicData.findtext('SexoParlamentar')
    email = basicData.findtext('EmailParlamentar')
    photoUrl = basicData.findtext('UrlFotoParlamentar')

    termData = senator.find('Mandato')
    state = termData.findtext('UfParlamentar')
    initialDate = termData.find('PrimeiraLegislaturaDoMandato').findtext('DataInicio')
    finalDate = termData.find('SegundaLegislaturaDoMandato').findtext('DataFim')
    #the dates on the senate's API are already on the yyyy-mm-dd format, no need for formatting
    #it is supposed that all the senators have well-defined initial and final dates for their terms

    i += 1
    print('Downloading detailed info from Senator ' + politicalName + ' (' + str(i) + '/' +
                                    str(len(senatorsDataTree)) + ')')


    senatorReader = urllib2.urlopen('http://legis.senado.leg.br/dadosabertos/senador/' + senateId)
    senatorXml = senatorReader.read()
    senatorDataTree = ElementTree.fromstring(senatorXml)

    birthDate = senatorDataTree.find('Parlamentar').find('DadosBasicosParlamentar').findtext('DataNascimento')

    print('Inserting info from Senator ' + politicalName + ' into database...')
    newPerson = PersonDTO(name, politicalName, birthDate, gender, email, photoUrl)
    personId = PersonDAO.insertPersonOnDB(newPerson)

    newSenatorTerm = SenatorTermDTO(senateId, personId, state, initialDate, finalDate)
    SenatorTermDAO.insertTermOnDB(newSenatorTerm)
