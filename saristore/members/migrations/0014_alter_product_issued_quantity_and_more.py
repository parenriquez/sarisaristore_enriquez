# Generated by Django 4.1 on 2022-08-10 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_alter_product_issued_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='issued_quantity',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='received_quantity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date_of_purchase',
            field=models.CharField(blank=True, default=datetime.datetime(2022, 8, 10, 15, 12, 30), max_length=255, null=True),
        ),
    ]
