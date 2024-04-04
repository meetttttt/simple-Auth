"""
This is the main.py file for api routes
"""
import os
import logging

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS

import utils

# loading flask
app = Flask(__name__)

# loading env
load_dotenv()

# Enable CORS for all routes
CORS(app)


# Set up logging
logging.basicConfig(filename=os.getenv("LOG_FILE"),
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@app.route("/", methods=["GET"])
def index():
    logging.info(f"Index route hit")
    return jsonify({"message": "Index Route..!"}), 200

@app.route("/login", methods=["POST"])
def login():
    try:
        logging.info(f"Login route hit")
        data = request.get_json()  # get the data
        authResult = utils.user_auth(userName=data['userName'],
                                     userPassword=data['userPassword'])
        if authResult:
            return jsonify({"message": "Login Success",
                            "authResult": authResult}), 200
        else:
            return jsonify({"message": "Login Failed",
                            "authResult": authResult}), 200
    except Exception as e:
        logging.error(f"Error occurred:[main.py] {e}")
        return jsonify({"message": f"Error: {e}",
                        "authResult": "Failed"}), 500


if __name__ == "__main__":
    app.run(debug=False,
            port=5000,
            host="0.0.0.0")
