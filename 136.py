from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)
@app.route("/")

def index():
    return jsonify({
        "data": data,
        "message": "success"
    }),200

@app.route("/Star")

def star():
    name = request.args.get("Name")
    star_data = next(item for item in data if item["Name"] == name)
    return jsonify({
        "data": star_data,
        "message": "success"
    }),200


app.run()