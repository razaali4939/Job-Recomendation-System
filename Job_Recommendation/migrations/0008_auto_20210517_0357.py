# Generated by Django 3.2 on 2021-05-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_Recommendation', '0007_rename_sno_userresumes_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresumes',
            name='user',
        ),
        migrations.AlterField(
            model_name='userresumes',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
