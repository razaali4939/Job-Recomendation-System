# Generated by Django 3.2 on 2021-05-09 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Job_Recommendation', '0002_userresumes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresumes',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
