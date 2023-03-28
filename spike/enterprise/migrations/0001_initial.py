# Generated by Django 4.1.7 on 2023-03-27 00:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*', 'Sólo se permiten letras.')], verbose_name='nombre')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='email')),
                ('phone', models.PositiveBigIntegerField(null=True, verbose_name='telefono')),
                ('active', models.BooleanField(default=False, help_text='tramite activo', verbose_name='activo')),
            ],
        ),
    ]
