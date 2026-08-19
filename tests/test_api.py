from fastapi.testclient import TestClient
from app.main import app


def test_api_out_of_scope_and_objection():
    client = TestClient(app)
    r = client.post('/api/session')
    assert r.status_code == 200
    sid = r.json()['session_id']

    r = client.post('/api/message', json={
        'session_id': sid,
        'text': "What is the company's current stock price?",
    })
    assert r.status_code == 200
    assert "don't have that information" in r.json()['response'].lower()
    assert r.json()['answers'] == {}

    r = client.post('/api/message', json={
        'session_id': sid,
        'text': 'Why do you need my degree information?',
    })
    assert r.status_code == 200
    assert 'recruiter' in r.json()['response'].lower()
