import pytest
from flask_joke import web


@pytest.fixture
def client():
    web.app.config['TESTING'] = True
    client = web.app.test_client()
    yield client


def test_index_returns_code_200(client):
    response = client.get('/')
    assert response.status_code == 200


def test_index_returns_joke(client):
    response = client.get('/')
    s = '<p>Wenn ist das Nunstück git und Slotermeyer? Ja! ... <strong>Beiherhund</strong> '\
        'das Oder die Flipperwaldt gersput.</p>'.encode('utf-8')
    assert s in response.data

def test_from_json_returns_code_200(client):
    response = client.get('/from_json')
    assert response.status_code == 200


def test_from_json_returns_joke(client):
    response = client.get('/from_json')
    s = '<p>Wenn ist das Nunstück git und Slotermeyer? Ja! ... <strong>Beiherhund</strong> '\
        'das Oder die Flipperwaldt gersput.</p>'.encode('utf-8')
    assert s in response.data
