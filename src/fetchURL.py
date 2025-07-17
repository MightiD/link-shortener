import json

jsonPath = "../data/links.json"

def fetchUrl(shortened):
    with open(jsonPath, 'r') as file:
        json_data = json.load(file)
    try:
        link = json_data[shortened]
        return link
    except:
        return "link not found"
