from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField('возраст', default=18)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    def basket_price(self):
        return sum(el.product_cost for el in self.basket.all())

    def basket_qty(self):
        return sum(el.qty for el in self.basket.all())


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    NONBINARY = 'N'

    GENDER_CHOICES = (
        (MALE, 'M'),
        (FEMALE, 'F'),
        (NONBINARY, 'N')
    )

    user = models.OneToOneField(ShopUser, db_index=True, unique=True, null=False,
                                on_delete=models.CASCADE, related_name='profile')
    tagline = models.CharField(verbose_name='тэги', blank=True, max_length=128)
    about_me = models.TextField(verbose_name='о себе', blank=True, max_length=512)
    gender = models.CharField(verbose_name='пол', blank=True, max_length=1, choices=GENDER_CHOICES)

    @receiver(post_save, sender=ShopUser)
    def create_or_save_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)
        else:
            instance.profile.save()
