# Generated by Django 3.2 on 2021-05-09 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Job_Recommendation', '0003_alter_userresumes_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresumes',
            name='user',
        ),
    ]
