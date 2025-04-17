def test_healthz(client):
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json == {
        "application": "chassis",
        "status": "healthy",
        "version": "0.1.0",
    }


def test_boomz(client):
    response = client.get("/boomz")

    assert response.status_code == 500
    assert response.json == {
        "extra": {
            "exc_class": "RuntimeError",
            "exc_info": "💥 BOOM 💥",
        },
        "message": "💥 BOOM 💥",
        "status": 500,
    }


def test_not_found(client):
    response = client.get("/nonexistent-endpoint")

    assert response.status_code == 404
    assert response.json == {
        "extra": {
            "exc_class": "NotFound",
            "exc_info": (
                "404 Not Found: "
                "The requested URL was not found on the server. "
                "If you entered the URL manually please check your spelling "
                "and try again."
            ),
        },
        "message": (
            "The requested URL was not found on the server. "
            "If you entered the URL manually please check your spelling "
            "and try again."
        ),
        "status": 404,
    }
