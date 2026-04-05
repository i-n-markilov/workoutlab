from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from accounts.models import Profile
from accounts.forms import ProfileForm

UserModel = get_user_model()

class AccountSignalTests(TestCase):
    def setUp(self):
        Group.objects.get_or_create(name="User")

    def test_create_profile_and_assign_group_signal(self):
        user = UserModel.objects.create_user(username='testuser', email='test@test.com', password='password')

        self.assertTrue(Profile.objects.filter(user=user).exists())

        self.assertTrue(user.groups.filter(name='User').exists())

    def test_profile_form_sync_to_user(self):
        user = UserModel.objects.create_user(username='syncuser', email='sync@test.com', password='password')
        profile = Profile.objects.get(user=user)
        
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
        }
        form = ProfileForm(data=data, instance=profile)
        self.assertTrue(form.is_valid())
        form.save()
        
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
