# Generated by Django 3.2 on 2021-05-24 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_Recommendation', '0008_auto_20210517_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresumes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
