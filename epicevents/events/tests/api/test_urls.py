import pytest


@pytest.mark.parametrize('path', (
    '/fake_url/',
    '/api/clients/3/',
    '/api/contracts/3/',
    '/api/events/3/',
    '/api/clients/1/fake_action/',
    '/api/contracts/1/fake_action/',
    '/api/events/1/fake_action/',
))
def test_url_does_not_exists(path,  admin_client):
    response = admin_client.get(path)
    assert response.status_code == 404
