import subprocess
import csv
import requests
from clint.textui import progress

def download_file(url,folder):
	local_filename = folder+url.split('/')[-1]
	# NOTE the stream=True parameter
	print "Downloading %s" % local_filename
	r = requests.get(url, stream=True)
	with open(local_filename, 'wb') as f:
		total_length = int(r.headers.get('content-length'))
		for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
			if chunk: # filter out keep-alive new chunks
				f.write(chunk)
				f.flush() #commented by recommendation from J.F.Sebastian
	return local_filename


#clean the files folder
subprocess.call("rm -rf files", shell=True, cwd="../crawlers/")
subprocess.call("mkdir files", shell=True, cwd="../crawlers/")
#runs the crawler
cmdscrappy = "scrapy crawl parties-crawler -o ./files/parties.csv -t csv"
p = subprocess.call(cmdscrappy.split(), shell=False, cwd="../crawlers")


crawled_file = '../crawlers/files/parties.csv'
with open(crawled_file) as csvfile:
	reader = csv.DictReader(csvfile)
	row = next(reader) #csv has just one row
	states = row['states'].split(",")
	parties = row['parties'].split(",")
	link = row['link']
	links = []
	for state in states:
		volatile_slink = link
		volatile_slink = volatile_slink.replace("state", state)
		for party in parties:
			volatile_plink = volatile_slink
			volatile_plink = volatile_plink.replace("party", party)
			links.append(volatile_plink)

for link in links:
	download_file(link,"../crawlers/files/")
