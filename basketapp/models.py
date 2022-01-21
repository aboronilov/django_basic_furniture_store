from django.contrib.auth import get_user_model
from django.db import models

from mainapp.models import Product


class BasketItem(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField('количество', default=0)
    add_dt = models.DateTimeField('время', auto_now_add=True)
    update_dt = models.DateTimeField('время', auto_now=True)

    @classmethod
    def get_items(cls, user):
        return BasketItem.objects.filter(user=user)

    @property
    def product_cost(self):
        return self.product.price * self.qty

    @property
    def total_quantity(self):
        items = BasketItem.objects.filter(user=self.user)
        total_quantity = sum(list(map(lambda x: x.qty, items)))
        return total_quantity

    @property
    def total_cost(self):
        items = BasketItem.objects.filter(user=self.user)
        total_cost = sum(list(map(lambda x: x.qty * x.product.price, items)))
        return total_cost
