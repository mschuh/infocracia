import xml.etree.ElementTree as ElementTree
import urllib2
from db_connection import DbConnection

deputiesReader = urllib2.urlopen('http://www.camara.gov.br/SitCamaraWS/Deputados.asmx/ObterDeputados')
deputiesXml = deputiesReader.read()
deputiesDataTree = ElementTree.fromstring(deputiesXml)

print ElementTree.tostring(deputiesDataTree)
