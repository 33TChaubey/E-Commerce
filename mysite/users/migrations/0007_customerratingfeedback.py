# Generated by Django 4.2.2 on 2024-02-19 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_cartitem_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRatingFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_code', models.IntegerField(default=1)),
                ('ratings', models.FloatField(default=0.0)),
                ('feedback', models.TextField()),
                ('username', models.CharField(max_length=255)),
            ],
        ),
    ]
