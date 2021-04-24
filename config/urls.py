from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from epicevents.basic_admin.admin import basic_admin_site


urlpatterns = [
    path('auth-token/', obtain_auth_token),
    path('api/', include('config.api_router')),
    path('django-admin/', admin.site.urls),
    path('api-admin/', basic_admin_site.urls),
]
