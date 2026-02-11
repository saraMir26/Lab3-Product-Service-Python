from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ENABLE CORS
CORS(app)

port = int(os.environ.get("PORT", 3030))

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify([
        { "id": 1, "name": "Dog Food", "price": 19.99 },
        { "id": 2, "name": "Cat Food", "price": 34.99 },
        { "id": 3, "name": "Bird Seeds", "price": 10.99 },
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
