from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


def get_expiry_date():
    return now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField('возраст', null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    activation_key = models.CharField(verbose_name='ключ активации', max_length=128, null=True)
    activation_key_expiry = models.DateTimeField(verbose_name='активация истекает',
                                                 max_length=128,
                                                 default=get_expiry_date)

    def basket_price(self):
        return sum(el.product_cost for el in self.basket.all())

    def basket_qty(self):
        return sum(el.qty for el in self.basket.all())

    def is_activation_expired(self):
        return self.activation_key_expiry < now()
