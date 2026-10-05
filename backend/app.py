from flask import Flask, jsonify
from backend.impact_api import impact_api

app = Flask(__name__)

# Impact Analysis API
app.register_blueprint(impact_api)


@app.route("/")
def home():
    return jsonify({
        "message": "ChaosAgent AI is running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(debug=True)