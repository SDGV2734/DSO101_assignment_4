import os

from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Return a basic health response for the CST Booking System API."""
    return jsonify(
        {
            "status": "success",
            "message": "CST Booking System API is running live!",
        }
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
