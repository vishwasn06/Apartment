# Generated by Django 3.2.7 on 2021-10-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(error_messages={'unique': 'The Geeks Field you entered is not unique.'}, max_length=8, unique=True),
        ),
    ]
