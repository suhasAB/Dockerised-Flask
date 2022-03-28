import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello from Dockerized Flask app deployed on GCP</h1>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))