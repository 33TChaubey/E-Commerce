# Generated by Django 5.0.1 on 2024-02-06 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_itempictures'),
    ]

    operations = [
        migrations.CreateModel(
            name='CusOrders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_code', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
