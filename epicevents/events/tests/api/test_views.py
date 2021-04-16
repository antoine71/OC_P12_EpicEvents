from ...models import Client, Contract, Event

from django.test.client import encode_multipart


def test_create_client(random_sales_client, random_sales_user):
    client = random_sales_client
    nb_clients = Client.objects.count()
    path = '/api/clients/'
    response = client.post(
        path,
        data={
            'first_name': 'new_client',
            'last_name': 'new_client',
            'company_name': 'new_client',
            },
        )
    new_client = Client.objects.latest('date_created')
    assert new_client.sales_contact == random_sales_user
    assert Client.objects.count() == nb_clients + 1
    assert response.status_code == 201


def test_update_client(sales_client_owner_client_1):
    client = sales_client_owner_client_1
    path = '/api/clients/1/'
    data = {
        'first_name': 'new_client',
        'last_name': 'new_client',
        'company_name': 'new_client',
    }
    content = encode_multipart('BoUnDaRyStRiNg', data)
    content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
    response = client.put(path, content, content_type=content_type)
    assert response.status_code == 200


def test_delete_client(sales_client_owner_client_1):
    client = sales_client_owner_client_1
    path = '/api/clients/1/'
    nb_clients = Client.objects.count()
    nb_contracts = Contract.objects.count()
    contracts_pk = [contract.pk for contract in Contract.objects.filter(client=Client.objects.get(pk=1))]
    response = client.delete(path)
    for contract_pk in contracts_pk:
        assert not Contract.objects.filter(pk=contract_pk).exists()
    assert Client.objects.count() == nb_clients - 1
    assert Contract.objects.count() == nb_contracts - len(contracts_pk)
    assert response.status_code == 204


def test_create_contract(sales_client_owner_client_1):
    client = sales_client_owner_client_1
    nb_contracts = Contract.objects.count()
    path = '/api/clients/1/add_contract/'
    response = client.post(
        path,
        data={},
        )
    new_contract = Contract.objects.latest('date_created')
    assert new_contract.client == Client.objects.get(pk=1)
    assert Contract.objects.count() == nb_contracts + 1
    assert response.status_code == 201


def test_update_contract(sales_client_owner_client_1):
    client = sales_client_owner_client_1
    path = '/api/contracts/1/'
    data = {'amount': 1000, 'signed': True}
    content = encode_multipart('BoUnDaRyStRiNg', data)
    content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
    response = client.put(path, content, content_type=content_type)
    assert response.status_code == 200


def test_delete_contract(sales_client_owner_client_1):
    client = sales_client_owner_client_1
    path = '/api/contracts/1/'
    nb_contracts = Contract.objects.count()
    nb_events = Event.objects.count()
    event_pk = 1
    response = client.delete(path)
    assert Contract.objects.count() == nb_contracts - 1
    assert not Event.objects.filter(pk=event_pk).exists()
    assert Event.objects.count() == nb_events - 1
    assert response.status_code == 204


def test_create_event(sales_client_owner_client_1):
    client = sales_client_owner_client_1
    nb_events = Event.objects.count()
    path = '/api/contracts/2/add_event/'
    response = client.post(
        path,
        data={},
        )
    new_event = Event.objects.latest('date_created')
    assert new_event.pk == 2
    assert Event.objects.count() == nb_events + 1
    assert response.status_code == 201


def test_create_event_fails_if_contract_has_already_an_event(sales_client_owner_client_1):
    client = sales_client_owner_client_1
    path = '/api/contracts/1/add_event/'
    response = client.post(
        path,
        data={},
        )
    assert response.status_code == 400


def test_update_event(support_client_owner_event_1):
    client = support_client_owner_event_1
    path = '/api/events/1/'
    data = {'attendees': 1000, 'completed': True}
    content = encode_multipart('BoUnDaRyStRiNg', data)
    content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'
    response = client.put(path, content, content_type=content_type)
    assert response.status_code == 200


def test_delete_event(support_client_owner_event_1):
    client = support_client_owner_event_1
    path = '/api/events/1/'
    nb_events = Event.objects.count()
    response = client.delete(path)
    assert Event.objects.count() == nb_events - 1
    assert response.status_code == 204
