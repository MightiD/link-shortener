import hashlib
import json

jsonPath = "../data/links.json"

urlSchemes = ["http://", "https://", "HTTP://", "HTTPS://"]

def storeUrl(url, shortened):
    # read file
    with open(jsonPath) as file:
        jsonData = json.load(file)
    
    # update file
    jsonData.update({shortened: url})

    # write to file
    with open(jsonPath, "w") as file:
        json.dump(jsonData, file, indent=4)

def encodeUrl(url):
    # if url starts with any of the url schemes
    if url.startswith(tuple(urlSchemes)):
        # removes only first instance of that url scheme being found
        url.replace(tuple(urlSchemes), "", 1)
    
    print(url)
    
    sha = hashlib.sha1(url.encode()).hexdigest()
    # storeUrl(url, sha)
    return sha
