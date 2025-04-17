from flask import Flask
from werkzeug.exceptions import HTTPException

from chassis.api.blueprint import blueprint
from chassis.api.errors import handle_exception
from chassis.api.errors import handle_http_exception


def create_app() -> Flask:
    """Create and configure the Flask application instance."""
    app = Flask("chassis", static_folder=None)
    register_blueprints(app)
    register_error_handlers(app)
    return app


def register_blueprints(app: Flask) -> None:
    """Register all blueprints with the application."""
    app.register_blueprint(blueprint)


def register_error_handlers(app: Flask) -> None:
    """Configure global exception handlers for the application."""
    app.register_error_handler(HTTPException, handle_http_exception)
    app.register_error_handler(Exception, handle_exception)
