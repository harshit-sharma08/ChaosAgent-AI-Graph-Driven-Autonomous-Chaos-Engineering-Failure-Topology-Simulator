import networkx as nx
import pytest

from backend.chaos_engine import (
    FAILURE_TYPES,
    select_random_node,
    select_failure_type,
    inject_failure
)


def create_test_graph():
    graph = nx.DiGraph()

    graph.add_node("frontend")
    graph.add_node("api")
    graph.add_node("database")

    graph.add_edge("frontend", "api")
    graph.add_edge("api", "database")

    return graph


def test_select_random_node():
    graph = create_test_graph()

    node = select_random_node(graph)

    assert node in graph.nodes


def test_select_failure_type():
    failure = select_failure_type()

    assert failure in FAILURE_TYPES


def test_inject_failure_with_given_node():
    graph = create_test_graph()

    result = inject_failure(graph, "api")

    assert result["failed_node"] == "api"
    assert result["failure_type"] in FAILURE_TYPES


def test_inject_failure_random_node():
    graph = create_test_graph()

    result = inject_failure(graph)

    assert result["failed_node"] in graph.nodes
    assert result["failure_type"] in FAILURE_TYPES


def test_invalid_node():
    graph = create_test_graph()

    with pytest.raises(ValueError):
        inject_failure(graph, "invalid-service")