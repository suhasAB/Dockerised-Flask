import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello from Flask app deployed on GCP by Suhas Anand </h1> <br> <h2>CMPE 281 Lab 2- Deploying Flask on GCP</h2>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))