"""
Custom migration to create groups required to run the API.
"""
from django.db import migrations


def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    for group_name in ('sales', 'support', 'managers'):
        group = Group(name=group_name)
        group.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
