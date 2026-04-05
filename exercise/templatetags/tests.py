from django.template import Context, Template
from django.test import TestCase

class DifficultyBarTemplateTagTests(TestCase):
    def test_difficulty_bar_easy(self):
        template = Template('{% load difficulty_bar %}{% difficulty_bar "Easy" %}')
        rendered = template.render(Context())
        self.assertIn('bg-green-500', rendered)

    def test_difficulty_bar_medium(self):
        template = Template('{% load difficulty_bar %}{% difficulty_bar "Medium" %}')
        rendered = template.render(Context())
        self.assertIn('bg-yellow-500', rendered)

    def test_difficulty_bar_hard(self):
        template = Template('{% load difficulty_bar %}{% difficulty_bar "Hard" %}')
        rendered = template.render(Context())
        self.assertIn('bg-red-500', rendered)
