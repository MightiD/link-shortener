from flask import Flask, redirect, render_template
from encodeURL import encodeUrl
from fetchURL import fetchUrl

app = Flask(__name__)

SERVER_URL = "192.168.100.100:5000"

@app.route("/hello-world")
def helloWorld():
    return "Hello world!"

@app.route("/api/v1/encode/<string:url>")
def encode(url):
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
