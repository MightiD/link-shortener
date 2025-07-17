from flask import Flask, redirect, render_template, request
from encodeURL import encodeUrl
from fetchURL import fetchUrl

app = Flask(__name__)

SERVER_URL = "192.168.100.100:5000"

@app.route("/hello-world")
def helloWorld():
    return "Hello world!"

@app.route("/api/v1/encode/")
def encode():
    #?url={insert url here}
    url = request.args.get("url")
    return(f"{SERVER_URL}/{encodeUrl(url)}")

@app.route("/<string:url>")
def fetch(url):    
    fetched = fetchUrl(url)

    if fetched == "link not found":
        return fetched
    else:
        return redirect(f"http://{fetchUrl(url)}")

@app.route("/")
def rootPage():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

#TODO: when redirecting, either remove the http from all links before encoding, or account for links already having it there
#TODO: make a good user interface, should allow text input which fetches from the encode url
#TODO: dockerise
#TODO: remove hard coded urls and values (server url, json path)
#TODO: in UI allow seeing which links have been stored, and allow deletion of links
#TODO: if deploying on vps one day, create accounts feature
