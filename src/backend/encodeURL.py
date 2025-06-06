import hashlib
import json

jsonPath = "../../data/links.json"

def storeUrl(url, shortened):
    with open(jsonPath, 'r') as file:
        json_data = json.load(file)
    json_data[shortened] = url
    with open(jsonPath, 'w') as file:
        json.dump(json_data, file, indent=4)
    

def encodeUrl(url):
    sha = hashlib.sha1(url.encode()).hexdigest()
    storeUrl(url, sha)
    return sha