import pytest

from . import api_endpoints


@pytest.mark.parametrize(
    'endpoint',
    api_endpoints.API_ENDPOINTS,
    ids=[endpoint['path'] for endpoint in api_endpoints.API_ENDPOINTS],
    )
def test_access_not_authorized_for_anonymous_user(endpoint, client):
    c = client
    for method in endpoint['methods']:
        response = getattr(c, method['name'])(endpoint['path'])
        assert response.status_code == 401


@pytest.mark.parametrize(
    'endpoint',
    api_endpoints.API_ENDPOINTS,
    ids=[endpoint['path'] for endpoint in api_endpoints.API_ENDPOINTS],
    )
def test_access_authorized_for_authenticated_random_users(endpoint, random_client):
    c = random_client
    for method in endpoint['methods']:
        if 'all' in method['permissions']:
            response = getattr(c, method['name'])(endpoint['path'])
            assert response.status_code != 403


@pytest.mark.parametrize(
    'endpoint',
    api_endpoints.API_ENDPOINTS,
    ids=[endpoint['path'] for endpoint in api_endpoints.API_ENDPOINTS],
    )
def test_access_not_authorized_for_authenticated_random_users(endpoint, random_client):
    c = random_client
    for method in endpoint['methods']:
        if 'all' not in method['permissions']:
            response = getattr(c, method['name'])(endpoint['path'])
            assert response.status_code == 403


@pytest.mark.parametrize(
    'endpoint',
    api_endpoints.API_ENDPOINTS,
    ids=[endpoint['path'] for endpoint in api_endpoints.API_ENDPOINTS],
    )
def test_access_authorized_for_sales_users(endpoint, random_sales_client):
    c = random_sales_client
    for method in endpoint['methods']:
        if 'sales' in method['permissions']:
            response = getattr(c, method['name'])(endpoint['path'])
            assert response.status_code != 403


@pytest.mark.parametrize(
    'endpoint',
    api_endpoints.API_ENDPOINTS,
    ids=[endpoint['path'] for endpoint in api_endpoints.API_ENDPOINTS],
    )
def test_access_authorized_for_objects_owned_by_sales_user(endpoint, sales_client_owner_client_1):
    for method in endpoint['methods']:
        if 'sales_user' in method['permissions']:
            response = getattr(sales_client_owner_client_1, method['name'])(endpoint['path'])
            assert response.status_code != 403
        elif 'support_user' in method['permissions']:
            response = getattr(sales_client_owner_client_1, method['name'])(endpoint['path'])
            assert response.status_code == 403


@pytest.mark.parametrize(
    'endpoint',
    api_endpoints.API_ENDPOINTS,
    ids=[endpoint['path'] for endpoint in api_endpoints.API_ENDPOINTS],
    )
def test_access_not_authorized_for_objects_not_owned_by_sales_user(endpoint, random_sales_client):
    for method in endpoint['methods']:
        if 'sales_user' in method['permissions']:
            response = getattr(random_sales_client, method['name'])(endpoint['path'])
            assert response.status_code == 403


@pytest.mark.parametrize(
    'endpoint',
    api_endpoints.API_ENDPOINTS,
    ids=[endpoint['path'] for endpoint in api_endpoints.API_ENDPOINTS],
    )
def test_access_authorized_for_objects_owned_by_support_user(endpoint, support_client_owner_event_1):
    for method in endpoint['methods']:
        if 'support_user' in method['permissions']:
            response1 = getattr(support_client_owner_event_1, method['name'])(endpoint['path'])
            assert response1.status_code != 403
        elif 'sales_user' in method['permissions']:
            response = getattr(support_client_owner_event_1, method['name'])(endpoint['path'])
            assert response.status_code == 403


@pytest.mark.parametrize(
    'endpoint',
    api_endpoints.API_ENDPOINTS,
    ids=[endpoint['path'] for endpoint in api_endpoints.API_ENDPOINTS],
    )
def test_access_not_authorized_for_objects_not_owned_by_support_user(endpoint, random_support_client):
    for method in endpoint['methods']:
        if 'support_user' in method['permissions']:
            response1 = getattr(random_support_client, method['name'])(endpoint['path'])
            assert response1.status_code == 403
