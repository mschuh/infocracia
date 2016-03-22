import xml.etree.ElementTree as ElementTree
import urllib2

from db_connection import *
from model import *

print('Downloading general agencies info...')
agenciesReader = urllib2.urlopen('http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterOrgaos')
agenciesXml = agenciesReader.read()
print('Parsing agencies\' information...')
agenciesDataTree = ElementTree.fromstring(agenciesXml)

agenciesList = []
i = 0
for agency in agenciesDataTree:
    agencyAttributes = agency.attrib
    chamberId = agencyAttributes['id']
    acronym = agencyAttributes['sigla'].strip()
    description = agencyAttributes['descricao']

    #TODO: on the next feature development, get correctly this info
    active = True

    print('Inserting info from ' + acronym + ' into the database...')
    newAgency = ChamberAgencyDTO(chamberId, acronym, description, active)
    ChamberAgencyDAO.insertAgencyOnDB(newAgency)

    print('Downloading member information from ' + acronym)
    agencyReader = urllib2.urlopen('http://www.camara.gov.br/SitCamaraWS/Orgaos.asmx/ObterMembrosOrgao?IDOrgao=' +
                                    chamberId)
    agencyXml = agencyReader.read()
    agencyMembers = agencyXml.find('membros')

    idPresident = agencyMembers.find('Presidente').findtext('ideCadastro')
    print('Inserting president ' + agencyMembers.find('Presidente').findtext('nome') + ' relation on the DB')
    idFirstVp = agencyMembers.find('PrimeiroVice-Presidente').findtext('ideCadastro')
    print('Inserting ')
    idSecondVp = agencyMembers.find('SegundoVice-Presidente').findtext('ideCadastro')
    idThirdVp = agencyMembers.find('TerceiroVice-Presidente').findtext('ideCadastro')
    idRapporteur = agencyMembers.find('Relator').findtext('ideCadastro')
