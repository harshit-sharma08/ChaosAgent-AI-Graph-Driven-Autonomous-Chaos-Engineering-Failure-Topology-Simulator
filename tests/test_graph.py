from backend.graph_engine import (
    create_topology,
    find_affected_services,
    calculate_severity
)


def test_database_failure_propagation():

    graph = create_topology()

    affected = find_affected_services(
        graph,
        "Database"
    )

    assert "Payment Service" in affected
    assert "Order Service" in affected
    assert "API Gateway" in affected
    assert "Frontend" in affected


def test_payment_failure_propagation():

    graph = create_topology()

    affected = find_affected_services(
        graph,
        "Payment Service"
    )

    assert "API Gateway" in affected
    assert "Frontend" in affected


def test_database_failure_severity():

    graph = create_topology()

    severity = calculate_severity(
        graph,
        "Database"
    )

    assert severity == "Critical"


def test_payment_failure_severity():

    graph = create_topology()

    severity = calculate_severity(
        graph,
        "Payment Service"
    )

    assert severity == "Critical"