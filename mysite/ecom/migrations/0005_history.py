# Generated by Django 5.0.1 on 2024-02-06 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_item_added_by_item_prod_code_item_saler_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('prod_code', models.IntegerField()),
                ('item_name', models.CharField(max_length=100)),
                ('operation_type', models.CharField(max_length=100)),
                ('user_type', models.CharField(max_length=100)),
            ],
        ),
    ]
