import pytest

from django.core.management import call_command


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'epicevents/events/tests/data.json')


@pytest.fixture
def random_user(django_user_model):
    username = "random_user"
    user = django_user_model.objects.get(username=username)
    return user


@pytest.fixture
def random_sales_user(django_user_model):
    username = "random_sales_user"
    user = django_user_model.objects.get(username=username)
    return user


@pytest.fixture
def sales_user_owner_client_1(django_user_model):
    username = "sales_user_owner_client_1"
    user = django_user_model.objects.get(username=username)
    return user


@pytest.fixture
def random_support_user(django_user_model):
    username = "random_support_user"
    user = django_user_model.objects.get(username=username)
    return user


@pytest.fixture
def support_user_owner_event_1(django_user_model):
    username = "support_user_owner_event_1"
    user = django_user_model.objects.get(username=username)
    return user


@pytest.fixture
def random_client(client, random_user):
    client.force_login(random_user)
    return client


@pytest.fixture
def random_sales_client(client, random_sales_user):
    client.force_login(random_sales_user)
    return client


@pytest.fixture
def sales_client_owner_client_1(client, sales_user_owner_client_1):
    client.force_login(sales_user_owner_client_1)
    return client


@pytest.fixture
def random_support_client(client, random_support_user):
    client.force_login(random_support_user)
    return client


@pytest.fixture
def support_client_owner_event_1(client, support_user_owner_event_1):
    client.force_login(support_user_owner_event_1)
    return client
