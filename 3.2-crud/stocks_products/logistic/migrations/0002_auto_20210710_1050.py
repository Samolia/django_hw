# Generated by Django 3.2.5 on 2021-07-10 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Склад', 'verbose_name_plural': 'Склады'},
        ),
    ]
