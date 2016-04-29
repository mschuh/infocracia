import datetime

from db_connection import *
from model import *
from helpers import *

gender_map = {'MASCULINO' : 'M', 'FEMININO' : 'F'}
executive_roles_regex = "(PRESIDENTE\"|GOVERNADOR\").*\"ELEITO\"" #it includes vice-governors and vice-presidents
for executive_member in filter_consulta_cand(executive_roles_regex):
    member_data = executive_member.split(';')
    name = member_data[10].replace("\"", "")
    political_name = member_data[14].replace("\"", "")
    birth_date_array = member_data[26].replace("\"", "").split("/")
    #format form dd/mm/yyyy to yyyy-mm-dd
    birth_date = '-'.join(reversed(birth_date_array))
    gender = gender_map[member_data[30].replace("\"", "")]
    profession = member_data[25].replace("\"", "")
    email = member_data[45].replace("\"", "").strip()
    if(email == "#NULO#"):
        email = u"N\xc3O DIVULGADO"

    state = member_data[5].replace("\"", "")
    seq_number = member_data[11].replace("\"", "") #internal sequential id for the candidate on TSE's system
    photo_url = "http://inter01.tse.jus.br/divulga-cand-2014/eleicao/2014/UF/" + state + "/foto/" + seq_number + ".jpg"

    initial_date = "2015-01-01"
    final_date = "2019-01-01"
    role = member_data[9].replace("\"", "")

    print('Inserting info from ' + role + ' ' + political_name + ' in the database.')
    new_person = PersonDTO(name, political_name, birth_date, gender, email, photo_url, profession)
    person_id = PersonDAO.insertPersonInDB(new_person)

    new_executive_term = ExecutiveTermDTO(person_id, state, initial_date, final_date, role)
    ExecutiveTermDAO.insertTermInDB(new_executive_term)
