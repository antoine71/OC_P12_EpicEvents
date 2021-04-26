from django.apps import AppConfig
from django.db.models.signals import post_migrate

from .management import create_permissions


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'epicevents.users'

    def ready(self):
        post_migrate.connect(create_permissions, sender=self)
