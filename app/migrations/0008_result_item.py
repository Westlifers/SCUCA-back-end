# Generated by Django 3.2.5 on 2022-03-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_competition_item_222'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='item',
            field=models.CharField(choices=[('222', '222'), ('333', '333'), ('444', '444'), ('555', '555'), ('666', '666'), ('777', '777'), ('sk', 'sk'), ('py', 'py'), ('sq1', 'sq1'), ('minx', 'minx'), ('clock', 'clock'), ('FMC', 'FMC'), ('333oh', '333oh'), ('333bf', '333bf'), ('444bf', '444bf'), ('555bf', '555bf')], default='333', max_length=10, verbose_name='参赛项目'),
        ),
    ]