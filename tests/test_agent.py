from backend.agent import detect_root_cause, analyze_failure


def test_root_cause_detection():

    root_cause = detect_root_cause(
        "Database",
        "Database Failure"
    )

    assert root_cause == "Database experienced Database Failure"


def test_failure_analysis():

    result = analyze_failure(
        "Database",
        "Database Failure",
        [
            "Payment Service",
            "Order Service",
            "API Gateway",
            "Frontend"
        ],
        "Critical"
    )

    assert result["root_cause"] == "Database experienced Database Failure"

    assert result["severity"] == "Critical"

    assert "Payment Service" in result["affected_services"]

    assert len(result["recovery_steps"]) > 0

    assert len(result["prevention"]) > 0
    