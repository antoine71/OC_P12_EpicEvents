"""
Custom migration to assign permissions to 'managers' group.
"""
import itertools

from django.db import migrations


def create_permissions(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    group = Group.objects.get(name='managers')
    for codename in [
        '_'.join((f, g)) for f, g in itertools.product(
            ['add','change', 'delete', 'view'],
            ['user', 'client', 'contract', 'event']
        )]:
        permission = Permission.objects.get(codename=codename)
        group.permissions.add(permission)
    group.save()



class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_data_migration_groups'),
    ]

    operations = [
        migrations.RunPython(create_permissions),        
    ]
