from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.admin import TokenAdmin

from ..basic_admin.admin import basic_admin_site

User = get_user_model()


class BasicUserAdmin(auth_admin.UserAdmin):

    managers_fieldsets = (
        (None, {"fields": ("username", "password", )}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", )}),
        (
            _("Permissions"),
            {
                "fields": (
                    'is_active',
                    "groups",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username",  'email', 'first_name', 'last_name']
    search_fields = ["username"]
    list_filter = ('groups', )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_superuser=False)

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_fieldsets(request, obj)
        else:
            return self.managers_fieldsets


basic_admin_site.register(User, BasicUserAdmin)
basic_admin_site.register(Group, auth_admin.GroupAdmin)
basic_admin_site.register(Token, TokenAdmin)
