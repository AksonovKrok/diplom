# Generated by Django 3.0.8 on 2021-05-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_remove_smartphone_processor_freq'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='processor_freq',
            field=models.CharField(default=0, max_length=255, verbose_name='Частота процессора'),
            preserve_default=False,
        ),
    ]