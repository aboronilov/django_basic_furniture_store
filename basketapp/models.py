from django.contrib.auth import get_user_model
from django.db import models

from mainapp.models import Product


class BasketItem(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.CASCADE,
                             related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('количество', default=0)
    add_dt = models.DateTimeField('время', auto_now_add=True)
    update_dt = models.DateTimeField('время', auto_now=True)

    # def delete(self, *args, **kwargs):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super().delete(*args, **kwargs)
    #
    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         old_basket_item = self.objects.get(pk=self.pk)
    #         self.product.quantity = self.quantity - old_basket_item.quantity
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super().save(*args, **kwargs)

    @classmethod
    def get_items(cls, user):
        return BasketItem.objects.filter(user=user)

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        items = BasketItem.objects.filter(user=self.user)
        total_quantity = sum(list(map(lambda x: x.quantity, items)))
        return total_quantity

    @property
    def total_cost(self):
        items = BasketItem.objects.filter(user=self.user)
        total_cost = sum(list(map(lambda x: x.quantity * x.product.price, items)))
        return total_cost
