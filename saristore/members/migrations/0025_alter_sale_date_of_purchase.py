# Generated by Django 4.1 on 2022-08-10 09:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0024_alter_product_issued_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date_of_purchase',
            field=models.CharField(blank=True, default=datetime.datetime(2022, 8, 10, 17, 41, 32), max_length=255, null=True),
        ),
    ]
