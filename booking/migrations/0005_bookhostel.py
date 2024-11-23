# Generated by Django 3.2.6 on 2022-05-01 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0004_remove_bed_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookHostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.bed')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.building')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
