from flask import Response
from werkzeug.exceptions import HTTPException

from chassis.api.components import Component


class Error(Component):
    """Represents an error response."""

    message: str
    status: int
    extra: dict


def make_response(error: Error) -> Response:
    """Creates a standardized JSON error response."""
    return Response(
        error.model_dump_json(),
        mimetype="application/json",
        status=error.status,
    )


def handle_http_exception(exception: HTTPException) -> Response:
    """Handles http exceptions by converting them to error responses."""
    return make_response(
        Error(
            message=exception.description or str(exception),
            status=exception.code or 500,
            extra={
                "exc_class": exception.__class__.__name__,
                "exc_info": str(exception),
            },
        )
    )


def handle_exception(exception: Exception) -> Response:
    """Handles generic exceptions by converting them to error responses."""
    return make_response(
        Error(
            message=str(exception),
            status=500,
            extra={
                "exc_class": exception.__class__.__name__,
                "exc_info": str(exception),
            },
        )
    )
