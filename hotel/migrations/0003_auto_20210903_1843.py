# Generated by Django 3.2.6 on 2021-09-03 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_rename_hotels_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(default='India', max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(default='Apartment', max_length=30),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(default='Karnataka', max_length=50),
        ),
    ]
