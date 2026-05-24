from app import app


def test_home_math_logic_structure():
    assert 2 + 2 == 4


def test_home_endpoint_returns_success_payload():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "success",
        "message": "CST Booking System API is running live!",
    }
