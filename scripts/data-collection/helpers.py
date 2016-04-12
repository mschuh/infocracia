import wikipedia
import requests
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
            for addkeyword in addkeywords:
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
