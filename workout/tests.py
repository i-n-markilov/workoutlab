from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from workout.validators import min_value_validator
from workout.forms import WorkoutExerciseForm, dynamic_workout_formset
from workout.models import WorkoutPlan
from exercise.models import Exercise

UserModel = get_user_model()

class ValidatorTests(TestCase):
    def test_min_value_validator_positive(self):
        try:
            min_value_validator(1)
        except ValidationError:
            self.fail("min_value_validator raised ValidationError unexpectedly!")

    def test_min_value_validator_zero(self):
        with self.assertRaises(ValidationError):
            min_value_validator(0)

    def test_min_value_validator_negative(self):
        with self.assertRaises(ValidationError):
            min_value_validator(-1)

class WorkoutFormTests(TestCase):
    def setUp(self):
        self.user1 = UserModel.objects.create_user(username='user1', email='u1@test.com', password='password')
        self.user2 = UserModel.objects.create_user(username='user2', email='u2@test.com', password='password')
        self.public_exercise = Exercise.objects.create(name='Public Ex', difficulty='Easy', primary_muscle_group='Chest', private=False)
        self.private_exercise = Exercise.objects.create(name='Private Ex', difficulty='Easy', primary_muscle_group='Chest', private=True, user=self.user1)

    def test_workout_exercise_form_filtering(self):
        form = WorkoutExerciseForm(user=self.user1)
        choices = [x[0] for x in form.fields['exercise'].choices]
        self.assertIn(self.public_exercise.pk, choices)
        self.assertIn(self.private_exercise.pk, choices)

        form2 = WorkoutExerciseForm(user=self.user2)
        choices2 = [x[0] for x in form2.fields['exercise'].choices]
        self.assertIn(self.public_exercise.pk, choices2)
        self.assertNotIn(self.private_exercise.pk, choices2)

    def test_dynamic_workout_formset_generation(self):
        plan = WorkoutPlan.objects.create(name='Test Plan', user=self.user1)
        formset = dynamic_workout_formset(plan, self.user1)
        self.assertEqual(len(formset.forms), 6)
