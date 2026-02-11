print(">>>> STARTING PRODUCT SERVICE <<<<")

from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Product service is running"

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify([...])

if __name__ == "__main__":
    app.run(host="0.0.0.0")
