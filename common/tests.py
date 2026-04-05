from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import models, connection
from common.managers import VisibilityQuerySet

UserModel = get_user_model()

class VisibilityModel(models.Model):
    name = models.CharField(max_length=100)
    private = models.BooleanField(default=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    objects = VisibilityQuerySet.as_manager()

    class Meta:
        app_label = 'common'

class VisibilityQuerySetTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(VisibilityModel)

    @classmethod
    def tearDownClass(cls):
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(VisibilityModel)
        super().tearDownClass()

    def setUp(self):
        self.user1 = UserModel.objects.create_user(username='user1', email='u1@test.com', password='password')
        self.user2 = UserModel.objects.create_user(username='user2', email='u2@test.com', password='password')
        self.public_item = VisibilityModel.objects.create(name='Public', private=False)
        self.private_item_u1 = VisibilityModel.objects.create(name='Private U1', private=True, user=self.user1)
        self.private_item_u2 = VisibilityModel.objects.create(name='Private U2', private=True, user=self.user2)

    def test_visible_for_user_authenticated(self):
        qs = VisibilityModel.objects.visible_for_user(self.user1)
        self.assertIn(self.public_item, qs)
        self.assertIn(self.private_item_u1, qs)
        self.assertNotIn(self.private_item_u2, qs)

    def test_visible_for_user_anonymous(self):
        class AnonymousUser:
            is_authenticated = False
            
        qs = VisibilityModel.objects.visible_for_user(AnonymousUser())
        self.assertIn(self.public_item, qs)
        self.assertNotIn(self.private_item_u1, qs)
        self.assertNotIn(self.private_item_u2, qs)

    def test_editable_by_user(self):
        qs = VisibilityModel.objects.editable_by_user(self.user1)
        self.assertIn(self.private_item_u1, qs)
        self.assertNotIn(self.private_item_u2, qs)
        self.assertNotIn(self.public_item, qs)
