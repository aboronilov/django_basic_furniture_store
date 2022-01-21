# Generated by Django 3.2.9 on 2022-01-21 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20220118_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopuserprofile',
            old_name='tag_line',
            new_name='tagline',
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]