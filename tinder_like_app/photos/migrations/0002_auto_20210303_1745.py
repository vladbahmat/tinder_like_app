# Generated by Django 3.1.6 on 2021-03-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.CharField(max_length=30),
        ),
    ]