"""
Small web server
===================
This is a tiny Flask Application uses as middleware, making it simple
to add cross origin support to this application.

"""

from flask import request, Flask, jsonify
from flask_cors import CORS
import requests, json

app = Flask(__name__)
app.config["DEBUG"] = True

cors = CORS(app, resources=r'/api/*', allow_headers='Content-Type')


@app.route('/', methods=['GET'])
def home():
    return "API Version 0.1"


@app.route("/api/v1/info", methods=['GET'])
def get_user_information():
    # Opening JSON file
    with open('data.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    return jsonify(json_object)


@app.route("/api/v1/users/<username>", methods=['GET'])
def get_user(username):
    content = requests.get("https://bio.torre.co/api/bios/" + username)
    data = json.loads(content.content)
    if content.ok:
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)
    return jsonify(data)


app.run()
