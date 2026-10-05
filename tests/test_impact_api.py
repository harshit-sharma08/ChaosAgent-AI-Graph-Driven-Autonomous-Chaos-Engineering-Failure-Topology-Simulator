from backend.app import app


def test_impact_api():

    client = app.test_client()

    response = client.post(
        "/impact",
        json={
            "service": "payment"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["failed_service"] == "payment"
    assert "database" in data["affected_services"]
    assert "notification" in data["affected_services"]
    assert "storage" in data["affected_services"]