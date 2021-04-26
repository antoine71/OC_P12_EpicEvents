import factory
from django.contrib.auth import get_user_model


class UserFactory(factory.Factory):

    username = 'johnsdoe'
    first_name = 'John'
    last_name = 'Doe'

    class Meta:
        model = get_user_model()

