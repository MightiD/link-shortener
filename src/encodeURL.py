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
    #if contains a url scheme
    if url.startswith(tuple(urlSchemes)):
        # removes every character up to the ://, then removes the ://
        url = url[url.find("://"):][3:]
    
    sha = hashlib.sha1(url.encode()).hexdigest()
    # storeUrl(url, sha)
    return sha
