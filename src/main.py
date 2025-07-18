from flask import Flask, redirect, render_template, request
from encodeURL import encodeUrl
from fetchURL import fetchUrl

app = Flask(__name__)

def getServerUrl():
    with open('../data/serverAddress.txt') as f: s = f.read()
    return s.strip()

@app.route("/hello-world")
def helloWorld():
    return "Hello world!"

@app.route("/api/v1/encode/")
def encode():
    #?url={insert url here}
    url = request.args.get("url")
    serverAdd = getServerUrl()
    return(f"{serverAdd}/{encodeUrl(url)}")

@app.route("/<string:url>")
def fetch(url):    
    fetched = fetchUrl(url)

    if fetched == "link not found":
        return fetched
    else:
        return redirect(f"http://{fetchUrl(url)}")

@app.route("/")
def index():
    return render_template("index.html")

def main():
    serverAdd = getServerUrl()
    if len(serverAdd) == 0:
        print("NO SERVER ADDRESS PROVIDED")
        return 1
    
    port = serverAdd[serverAdd.find(":"):][1:]

    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main()

#TODO: dockerise
#TODO: remove hard coded urls and values (server url, json path)
#TODO: in UI allow seeing which links have been stored, and allow deletion of links
#TODO: if deploying on vps one day, create accounts feature
