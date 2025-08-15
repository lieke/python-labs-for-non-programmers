import pytest
from answers.webapp import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, web!' in response.data

def test_message(client):
    response = client.get('/greeting?message=Hi&name=Alice')
    assert response.status_code == 200
    assert b'Hi, Alice!' in response.data

def test_message_default(client):
    response = client.get('/greeting')
    assert response.status_code == 200
    assert b'Hello, lovely human!' in response.data
