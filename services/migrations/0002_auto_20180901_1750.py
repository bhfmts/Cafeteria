# Generated by Django 2.0.2 on 2018-09-01 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created'], 'verbose_name': 'servicio', 'verbose_name_plural': 'servicios'},
        ),
    ]
