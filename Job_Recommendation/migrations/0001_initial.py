# Generated by Django 3.2 on 2021-05-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Dataset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('JobTitle', models.CharField(max_length=131)),
                ('Company', models.CharField(max_length=255)),
                ('Location', models.CharField(max_length=14)),
                ('PostDate', models.CharField(max_length=30)),
                ('ExtractDate', models.CharField(max_length=130)),
                ('Summary', models.CharField(max_length=131)),
                ('Salary', models.CharField(max_length=132)),
                ('JobUrl', models.CharField(max_length=133)),
            ],
        ),
        migrations.CreateModel(
            name='JobPublish',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('JobTitles', models.CharField(max_length=131)),
                ('Companys', models.CharField(max_length=255)),
                ('Locations', models.CharField(max_length=14)),
                ('PostDates', models.CharField(max_length=30)),
                ('Summarys', models.CharField(max_length=131)),
                ('Salarys', models.CharField(max_length=132)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=131)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=14)),
                ('role_select', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
                ('password', models.CharField(max_length=130)),
                ('again_password', models.CharField(max_length=131)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserResumes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=1000, null=True)),
                ('lastname', models.CharField(default='', max_length=50, null=True)),
                ('mobile', models.CharField(default='', max_length=100, null=True)),
                ('email', models.CharField(default='', max_length=50, null=True)),
                ('objective', models.CharField(default='', max_length=1000, null=True)),
                ('address', models.CharField(default='', max_length=5000, null=True)),
                ('skill', models.TextField(default='', max_length=5000, null=True)),
                ('companylocation', models.TextField(default='', max_length=5000, null=True)),
                ('experience', models.CharField(default='', max_length=3000, null=True)),
                ('description', models.TextField(default='', max_length=3000, null=True)),
                ('degreename1', models.CharField(default='', max_length=1000, null=True)),
                ('collegename', models.CharField(default='', max_length=1000, null=True)),
                ('marks', models.CharField(default='', max_length=100, null=True)),
                ('cgpas', models.CharField(default='', max_length=100, null=True)),
                ('degreename2', models.CharField(default='', max_length=1000, null=True)),
                ('universityname', models.CharField(default='', max_length=1000, null=True)),
            ],
        ),
    ]
