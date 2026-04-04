from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model

UserModel = get_user_model()

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission

    # Create groups
    user_group = Group.objects.get(name="User")
    moderator_group = Group.objects.get(name="Moderator")

    models = [
        ('equipment', 'equipment'),
        ('exercise', 'exercise'),
        ('workout', 'workoutplan'),
    ]

    user_perms = []
    moderator_perms = []

    for app_label, model_name in models:
        perms = Permission.objects.filter(
            content_type__app_label=app_label,
            content_type__model=model_name
        )
        moderator_perms.extend(perms)
        user_perms.extend(perms.filter(codename__in=[f'add_{model_name}', f'view_{model_name}']))

    appuser_perms = Permission.objects.filter(
        content_type__app_label='accounts',
        content_type__model='appuser'
    )
    moderator_perms.extend(appuser_perms.filter(codename__in=['change_appuser', 'view_appuser']))

    user_group.permissions.set(user_perms)
    moderator_group.permissions.set(moderator_perms)

@receiver(post_save, sender=UserModel)
def create_profile_and_assign_group(sender, instance, created, **kwargs):
    if not created:
        return

    from .models import Profile
    from django.contrib.auth.models import Group

    Profile.objects.get_or_create(user=instance)

    try:
        user_group = Group.objects.get(name="User")
        instance.groups.add(user_group)
    except Group.DoesNotExist:
        pass