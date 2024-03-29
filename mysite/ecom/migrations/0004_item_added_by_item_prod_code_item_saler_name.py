# Generated by Django 5.0.1 on 2024-02-06 18:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_item_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='added_by',
            field=models.CharField(default='user_name', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='prod_code',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='item',
            name='saler_name',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
