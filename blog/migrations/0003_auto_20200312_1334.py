# Generated by Django 2.0.2 on 2020-03-12 19:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200312_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 12, 19, 34, 34, 441499, tzinfo=utc), verbose_name='Fecha de Aplicación'),
        ),
    ]