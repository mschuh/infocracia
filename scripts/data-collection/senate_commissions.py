import xml.etree.ElementTree as ElementTree
import urllib2
import sys

from db_connection import *
from model import *

print('Downloading general commissions info...')
commissionsReader = urllib2.urlopen('http://legis.senado.leg.br/dadosabertos/dados/ComissoesPermanentes.xml')
commissionsXml = commissionsReader.read()
print('Parsing agencis\' information...')
commissionsDataTree = ElementTree.fromstring(commissionsXml).find('Colegiados')

i = 0
for commission in commissionsDataTree:
    senateId = commission.findtext('CodigoColegiado')
    acronym = commission.findtext('SiglaColegiado')
    name =  commission.findtext('NomeColegiado')

    #this script only consider permanet commissions, therefore they're all active
    active = True

    print('Inserting info from ' + name + ' into the database...')
    newCommission = SenateCommissionDTO(senateId, acronym, name, active)
    SenateCommissionDAO.insertCommissionOnDB(newCommission)
