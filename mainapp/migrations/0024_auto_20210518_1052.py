# Generated by Django 3.0.8 on 2021-05-18 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_auto_20210518_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographic',
            name='zoom',
            field=models.CharField(max_length=255, verbose_name='Оптический зум'),
        ),
    ]