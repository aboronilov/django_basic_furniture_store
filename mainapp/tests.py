from django.test import TestCase

from authapp.models import ShopUser


class ModelTests(TestCase):
    def test_user_has_age(self):
        user = ShopUser.objects.create(age=23)
        self.assertIsNotNone(user.age)