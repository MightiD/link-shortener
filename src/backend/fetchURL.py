import json

jsonPath = "../../data/links.json"

def fetchUrl(shortened):
    with open(jsonPath, 'r') as file:
        json_data = json.load(file)
        print(json_data)
    try:
        link = json_data[shortened]
        print(link)
        return link
    except:
        return "link not found"