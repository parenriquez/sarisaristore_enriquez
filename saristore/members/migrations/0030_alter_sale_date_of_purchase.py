# Generated by Django 4.1 on 2022-08-11 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0029_alter_sale_date_of_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date_of_purchase',
            field=models.CharField(blank=True, default=datetime.datetime(2022, 8, 11, 16, 57, 13), max_length=255, null=True),
        ),
    ]
