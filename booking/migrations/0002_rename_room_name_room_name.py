# Generated by Django 3.2.6 on 2022-04-30 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_name',
            new_name='name',
        ),
    ]
