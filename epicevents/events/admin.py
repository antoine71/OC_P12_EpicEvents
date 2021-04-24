from django.contrib import admin
from .models import Client, Contract, Event

from ..basic_admin.admin import basic_admin_site


basic_admin_site.register(Client)
basic_admin_site.register(Contract)
basic_admin_site.register(Event)

admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)
