import pytest
from ezbudget import create_app

@pytest.fixture()
def app():
    app = create_app('tests/test_config.py')
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
