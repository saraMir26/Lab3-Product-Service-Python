# NOTE: This code was generated with the assistance of AI (ChatGPT) for learning purposes.

from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify([
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ])

# DO NOT call app.run() in Azure
