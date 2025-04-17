from flask import Response


def get_boomz() -> Response:
    """Handles the `GET /boomz` endpoint."""
    raise RuntimeError("💥 BOOM 💥")
