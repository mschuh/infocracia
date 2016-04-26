import wikipedia
import requests
import os
import re
import shutil
import zipfile

from clint.textui import progress

def wiki_image(lang, query, addkeywords):
    """Download full size images from Wikipedia.
    Don't print or republish images without permission.
    """

    wikipedia.set_lang(lang)
    suggestion = wikipedia.search(query, results=1)
    try:
        page = wikipedia.page(suggestion)
    except wikipedia.exceptions.DisambiguationError as e:
        for option in e.options:
            found = False
            for addkeyword in addkeywrds:
                if addkeyword in option:
                    print option
                    page = wikipedia.page(option)
                    found = True
                    break
            if found:
                break
        else:
            page = wikipedia.page(e.options[0])

    #print page.images
    for image in page.images:
        if 'logo' in image:
            return image
    else:
        return page.images[0]

def download_file(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

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

def filter_consulta_cand(regex):
    """Download the full information from TSE candidates in temporary files and filter them by returning only the lines
    that match the passed regular expression in form of an array.
    """

    temporaryDirPath = os.path.dirname(__file__) + "/tmp/"
    #Download zip file
    candFile = download_file("http://agencia.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2014.zip",
        temporaryDirPath)

    print("Exctracting files...")
    candZip = zipfile.ZipFile(candFile, 'r')
    candZip.extractall(temporaryDirPath)
    candZip.close()
    print("Files exctracted.")

    candidates = []
    for fileName in os.listdir(temporaryDirPath):
        if re.search(".*\.txt", fileName): #if it is a txt file
            print("Search regular expression in " + fileName)
            with open(temporaryDirPath + fileName, 'r') as currentFile:
                for line in currentFile:
                    if re.search(regex, line):
                        candidates.append(line.decode('iso-8859-1'))

    shutil.rmtree(temporaryDirPath) #remove temporary folder
    return candidates
