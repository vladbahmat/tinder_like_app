# Generated by Django 3.1.6 on 2021-03-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='swipes',
            field=models.FloatField(),
        ),
    ]
