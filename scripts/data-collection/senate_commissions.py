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

    rolesMapping = {'PRESIDENTE' : 'P', 'VICE-PRESIDENTE' : 'V', 'RELATOR' : 'R'}
    specialMembersIds = []
    specialMembers = commission.find('Cargos')
    for specialMember in specialMembers:
        specialMemberId = specialMember.findtext('Http')
        fullRoleName = specialMember.findtext('Cargo')
        specialMemberRole = rolesMapping[fullRoleName]

        #some slots on the xml represent vacancies and therefore don't have ids
        if not specialMemberId:
            continue

        print('Inserting ' + fullRoleName + ' ' + specialMember.findtext('NomeParlamentar') + ' relation into DB')
        memberParticipation = SenateCommissionParticipationDTO(specialMemberId, senateId, specialMemberRole)
        SenateCommissionParticipationDAO.insertParticipationOnDB(memberParticipation)

        specialMembersIds.append(int(specialMemberId))

    membersBlocks = commission.find('MembrosBloco')

    for membersBlock in membersBlocks:
        actualMembers = membersBlock.find('Membros')
        for member in actualMembers:
            memberId = member.findtext('Http')

            #some slots on the xml represent vacancies and therefore don't have ids
            if not memberId:
                continue
            #in the xml the special members are included in the members' tree
            if int(memberId) not in specialMembersIds:
                print('Inserting member ' + member.findtext('NomeParlamentar') + ' relation into DB' )
                memberParticipation = SenateCommissionParticipationDTO(memberId, senateId, 'M')
                SenateCommissionParticipationDAO.insertParticipationOnDB(memberParticipation)
