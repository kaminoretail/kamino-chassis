import pytest

from chassis.app import create_app


@pytest.fixture(scope="session")
def app():
    """Create application for testing."""
    _app = create_app()
    yield _app


@pytest.fixture
def client(app):
    """Create a test client for testing."""
    with app.test_client() as client:
        yield client
