import pytest

from . import api_endpoints


@pytest.mark.parametrize(
    'endpoint',
    api_endpoints.API_ENDPOINTS,
    ids=[endpoint['path'] for endpoint in api_endpoints.API_ENDPOINTS]
)
def test_methods_not_authorized(endpoint, random_sales_client):
    client = random_sales_client
    all_methods = ('get', 'post', 'put', 'patch', 'delete')
    for method in endpoint['methods']:
        if method['name'] not in all_methods:
            response = getattr(client, method['name'])(endpoint['path'])
            assert response.status_code == 405
