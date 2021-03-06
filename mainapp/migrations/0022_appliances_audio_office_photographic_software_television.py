# Generated by Django 3.0.8 on 2021-05-18 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_tablet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Television',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Диагональ экрана')),
                ('display_type', models.CharField(max_length=255, verbose_name='Тип телевизора')),
                ('matrix_type', models.CharField(max_length=255, verbose_name='Тип матрицы')),
                ('resolution', models.CharField(max_length=255, verbose_name='Разрешение экрана')),
                ('light', models.CharField(max_length=255, verbose_name='Тип подсветки')),
                ('razv', models.CharField(max_length=255, verbose_name='Частота развёртки экрана')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('country', models.CharField(max_length=255, verbose_name='Страна производитель')),
                ('lang', models.CharField(max_length=255, verbose_name='Язык интерфейса')),
                ('product', models.CharField(max_length=255, verbose_name='Продукт')),
                ('platforma', models.CharField(max_length=255, verbose_name='Платформа')),
                ('num_of_user', models.CharField(max_length=255, verbose_name='Количество пользователей')),
                ('type_of_user', models.CharField(max_length=255, verbose_name='Тип пользователя')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photographic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('photo_type', models.CharField(max_length=255, verbose_name='Тип фотокамеры')),
                ('matrix_resolution', models.CharField(max_length=255, verbose_name='Разрешение матрицы')),
                ('size_of_matrix', models.CharField(max_length=255, verbose_name='Размер матрицы')),
                ('type_of_matrix', models.CharField(max_length=255, verbose_name='Тип матрицы')),
                ('light', models.CharField(max_length=255, verbose_name='Максимальная светочувствительность')),
                ('zoom', models.BooleanField(default=True, verbose_name='Оптический зум')),
                ('focus_distans', models.CharField(max_length=255, verbose_name='Фокусное расстояние')),
                ('count_of_to', models.CharField(blank=True, max_length=255, null=True, verbose_name='Количество точек автофокуса')),
                ('format_of_s', models.CharField(max_length=255, verbose_name='Форматы съемки')),
                ('mikrofon', models.CharField(max_length=255, verbose_name='Микрофон')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('tecnology', models.CharField(max_length=255, verbose_name='Технология печати')),
                ('pechat', models.CharField(max_length=255, verbose_name='Печать')),
                ('resolution', models.CharField(max_length=255, verbose_name='Макс разрешение печати dpi')),
                ('colors', models.CharField(max_length=255, verbose_name='Количество цветов печати')),
                ('wi_fi', models.CharField(max_length=255, verbose_name='Wi-Fi')),
                ('garantiya', models.BooleanField(default=True, verbose_name='Гарантийный срок')),
                ('weight', models.CharField(max_length=255, verbose_name='Вес')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('type_of_type', models.CharField(max_length=255, verbose_name='Тип')),
                ('power_of_satelit', models.CharField(max_length=255, verbose_name='Выходная мощность сателлитов')),
                ('power', models.CharField(max_length=255, verbose_name='Выходная мощность')),
                ('bluetooth', models.CharField(max_length=255, verbose_name='Bluetooth')),
                ('diametr_of_sab', models.CharField(max_length=255, verbose_name='Диаметр динамика сабвуфера')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Appliances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Вид уборки')),
                ('display_type', models.CharField(max_length=255, verbose_name='Тип пылесборника')),
                ('resolution', models.CharField(max_length=255, verbose_name='Потребляемая мощность Вт')),
                ('accum_volume', models.CharField(max_length=255, verbose_name='Выпускной фильтр')),
                ('ram', models.CharField(max_length=255, verbose_name='Объём пылесборника')),
                ('sd', models.BooleanField(default=True, verbose_name='Длина шнура')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
