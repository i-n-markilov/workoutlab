from django.db import migrations

def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')

    Group.objects.get_or_create(name="User")
    Group.objects.get_or_create(name="Moderator")

def remove_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name="User").delete()
    Group.objects.filter(name="Moderator").delete()

class Migration(migrations.Migration):
    initial = False

    dependencies = [
        ('accounts', '0001_initial'),
        ('equipment', '0001_initial'),
        ('exercise', '0001_initial'),
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups, reverse_code=remove_groups),
    ]