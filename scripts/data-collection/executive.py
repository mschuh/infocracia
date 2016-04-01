import urllib2

from db_connection import *
from model import *
import csv
import json

with open('Remuneracao.csv', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     header = True
     for row in spamreader:
         if header:
              header = False
              continue
         print "\n".join(row)
         break

tokenPortalTransp = 'pZ7EHmcf0Obb'
req = urllib2.Request('http://api.transparencia.org.br:80/sandbox/v1/partidos')
req.add_header('App-Token', tokenPortalTransp)
parties = urllib2.urlopen(req)
parties = parties.read()
parties = json.loads(parties)
states = ["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"]
politicians = []
for party in parties:
     print "Getting politicians of " + party["sigla"] + "..."
     for state in states:
          print(state+",", end="")
          req = urllib2.Request('http://api.transparencia.org.br:80/sandbox/v1/candidatos?estado='+state+'&partido='+party["partidoId"])
          req.add_header('App-Token', tokenPortalTransp)
          newPoliticians = urllib2.urlopen(req)
          newPoliticians = newPoliticians.read()
          politicians = politicians + json.loads(newPoliticians)
          
print politicians
