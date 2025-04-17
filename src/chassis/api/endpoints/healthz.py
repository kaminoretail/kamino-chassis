from importlib.metadata import version

from flask import Response

from chassis.api.components import Component


class HealthzResponse(Component):
    """Represents an healthz response."""

    application: str
    version: str
    status: str


def get_healthz() -> Response:
    """Handle the `GET /healthz` endpoint."""
    response = HealthzResponse(
        application="chassis",
        version=version("chassis"),
        status="healthy",
    )
    return Response(
        response.model_dump_json(),
        mimetype="application/json",
        status=200,
    )
