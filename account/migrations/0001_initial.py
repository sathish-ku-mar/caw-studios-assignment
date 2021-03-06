# Generated by Django 3.1.1 on 2020-09-07 09:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='The name of the user', max_length=200)),
                ('email', models.EmailField(help_text='A unique email id of the user', max_length=254, unique=True)),
                ('phone', models.CharField(help_text='The phone number of the user', max_length=15, validators=[django.core.validators.RegexValidator(message='Please Enter correct Contact no.', regex='^\\d{10,15}$')])),
                ('password', models.TextField(help_text='The hashed password of the user')),
                ('last_login', models.DateTimeField(blank=True, help_text='The last login of the user', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
