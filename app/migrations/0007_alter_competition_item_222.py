# Generated by Django 3.2.5 on 2022-03-18 14:11

import app.scrambler
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_competition_item_222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='item_222',
            field=models.JSONField(default=app.scrambler.scrambler, verbose_name='222'),
        ),
    ]