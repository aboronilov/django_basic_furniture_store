# Generated by Django 2.2 on 2021-02-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210128_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активность'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активность'),
        ),
    ]