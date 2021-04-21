# Generated by Django 3.2 on 2021-04-21 11:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_enrolled',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='pin',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(6)]),
        ),
    ]
