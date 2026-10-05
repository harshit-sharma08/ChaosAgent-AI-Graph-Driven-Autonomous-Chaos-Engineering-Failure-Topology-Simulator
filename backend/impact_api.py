from flask import Blueprint, request, jsonify
import networkx as nx

from backend.impact_analyzer import analyze_impact


impact_api = Blueprint("impact_api", __name__)


@impact_api.route("/impact", methods=["POST"])
def impact_analysis():

    data = request.get_json()

    failed_service = data.get("service")

    if not failed_service:
        return jsonify({
            "error": "service is required"
        }), 400

    graph = nx.DiGraph()

    graph.add_edge("payment", "database")
    graph.add_edge("payment", "notification")
    graph.add_edge("database", "storage")

    result = analyze_impact(graph, failed_service)

    return jsonify(result), 200