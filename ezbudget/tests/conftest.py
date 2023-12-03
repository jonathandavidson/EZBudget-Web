"""Defines fixtures available to all tests."""
import pytest
from ezbudget import create_app

@pytest.fixture()
def app():
    """Create and configure a new app instance for each test."""
    app_instance = create_app('tests/test_config.py')
    yield app_instance

@pytest.fixture()
# pylint: disable-next=redefined-outer-name
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture()
# pylint: disable-next=redefined-outer-name
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()
