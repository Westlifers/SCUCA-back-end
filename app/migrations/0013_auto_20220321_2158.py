# Generated by Django 3.2.5 on 2022-03-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20220319_1112'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Classmate',
        ),
        migrations.AddField(
            model_name='result',
            name='video',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='视频BV号'),
        ),
    ]