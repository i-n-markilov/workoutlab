from django.test import TestCase
from django.contrib.auth import get_user_model
from exercise.forms import ExerciseCreateForm

UserModel = get_user_model()

class ExerciseFormTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', email='test@test.com', password='password')

    def test_clean_invalid_muscle_groups(self):
        data = {
            'name': 'Test Exercise',
            'difficulty': 'Easy',
            'primary_muscle_group': 'Chest',
            'secondary_muscle_group': 'Chest',
        }
        form = ExerciseCreateForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)
        self.assertEqual(form.errors['__all__'][0], 'Primary and secondary muscle groups cannot be the same')

    def test_clean_valid_muscle_groups(self):
        data = {
            'name': 'Test Exercise',
            'difficulty': 'Easy',
            'primary_muscle_group': 'Chest',
            'secondary_muscle_group': 'Back',
        }
        form = ExerciseCreateForm(data=data)
        self.assertTrue(form.is_valid(), form.errors)
