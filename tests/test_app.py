import pytest
from app import app as flask_app

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client

def test_index_returns_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello World'

def test_health_returns_200(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_health_response_empty(client):
    response = client.get('/health')
    assert response.data == b''

def test_nonexistent_route_returns_404(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404