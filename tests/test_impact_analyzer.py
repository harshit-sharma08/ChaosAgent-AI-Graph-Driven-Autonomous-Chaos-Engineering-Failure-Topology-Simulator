import networkx as nx

from backend.impact_analyzer import analyze_impact


def test_impact_analysis():

    graph = nx.DiGraph()

    graph.add_edge("payment", "database")
    graph.add_edge("payment", "notification")
    graph.add_edge("database", "storage")

    result = analyze_impact(graph, "payment")

    assert result["failed_service"] == "payment"

    assert "database" in result["affected_services"]
    assert "notification" in result["affected_services"]
    assert "storage" in result["affected_services"]

    assert result["impact_count"] == 3