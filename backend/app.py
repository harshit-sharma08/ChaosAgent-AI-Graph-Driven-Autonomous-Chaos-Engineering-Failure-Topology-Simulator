from flask import Flask, jsonify
from flask_cors import CORS

from backend.graph_engine import get_topology


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "ChaosAgent AI is running"
    })


@app.route("/topology")
def topology():
    return jsonify(get_topology())


if __name__ == "__main__":
    app.run(debug=True)