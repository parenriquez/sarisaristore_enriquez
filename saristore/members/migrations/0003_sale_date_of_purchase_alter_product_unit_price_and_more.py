# Generated by Django 4.1 on 2022-08-10 05:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_product_category_name_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='date_of_purchase',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 10, 13, 5, 31, 927444), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='unit_price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
