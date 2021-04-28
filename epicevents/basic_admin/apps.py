from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class BasicAdminAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'epicevents.basic_admin'


class BasicAdminSiteConfig(AdminConfig):
    default_site = 'epicevents.basic_admin.admin.BasicAdminSite'
