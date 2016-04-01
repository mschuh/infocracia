import subprocess
import csv
import requests
import fnmatch
import os
import zipfile
import glob
from clint.textui import progress


file_top_dir = '../crawlers/files/'


def download_file(url, folder):
    local_filename = folder + url.split('/')[-1]
    # NOTE the stream=True parameter
    print "Downloading %s" % local_filename
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()  # commented by recommendation from J.F.Sebastian
    return local_filename


def setup():
    # clean the files folder
    subprocess.call("rm -rf files", shell=True, cwd="../crawlers/")
    subprocess.call("mkdir files", shell=True, cwd="../crawlers/")
    # runs the crawler
    cmdscrappy = "scrapy crawl parties-crawler -o ./files/parties.csv -t csv"
    p = subprocess.call(cmdscrappy.split(), shell=False, cwd="../crawlers")


def generate_links(crawled_file):
    with open(crawled_file) as csvfile:
        reader = csv.DictReader(csvfile)
        row = next(reader)  # csv has just one row
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
    return links


def download_zipfiles():
    for link in links:
        download_file(link, file_top_dir)


def get_csv_files():
    csv_dir = file_top_dir + 'csv/'

    for file in glob.glob(file_top_dir + '*.zip'):
        zf = zipfile.ZipFile(file, 'r')
        for name in zf.namelist():
            if name.endswith('.csv'):
                outfile = open(os.path.join(
                    csv_dir, os.path.basename(name)), 'wb')
                outfile.write(zf.read(name))
                outfile.flush()
                outfile.close()

    matches = []
    for root, dirnames, filenames in os.walk(file_top_dir):
        for filename in fnmatch.filter(filenames, '*.csv'):
            matches.append(os.path.join(root, filename))

get_csv_files()
