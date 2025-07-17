import hashlib
import json

jsonPath = "../data/links.json"

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
    sha = hashlib.sha1(url.encode()).hexdigest()
    storeUrl(url, sha)
    return sha
