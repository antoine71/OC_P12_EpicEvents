from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('auth-token/', obtain_auth_token),
    path('api/', include('config.api_router')),
    path('admin/', admin.site.urls),
]
