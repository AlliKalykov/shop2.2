# Generated by Django 3.2 on 2022-12-12 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20221209_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothesColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=100, verbose_name='Название цвета')),
                ('color_slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Цвет одежды',
                'verbose_name_plural': 'Цвета одежды',
            },
        ),
        migrations.CreateModel(
            name='ClothesSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cn', models.CharField(max_length=10, verbose_name='Китайский размер')),
                ('eu', models.CharField(max_length=10, verbose_name='Европейский размер')),
                ('us', models.CharField(max_length=10, verbose_name='Американский размер')),
            ],
            options={
                'verbose_name': 'Размер одежды',
                'verbose_name_plural': 'Размеры одежды',
            },
        ),
        migrations.CreateModel(
            name='ClothesInStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_count', models.PositiveIntegerField()),
                ('clothes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes_in_stock', to='main.clothes')),
                ('clothes_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes_in_stock', to='main.clothescolor')),
                ('clothes_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes_in_stock', to='main.clothessize')),
            ],
            options={
                'verbose_name': 'Одежда в наличии',
                'verbose_name_plural': 'Одежда в наличии',
            },
        ),
    ]