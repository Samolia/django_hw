# Generated by Django 3.2.5 on 2021-07-07 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'verbose_name': 'температура'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'проект', 'verbose_name_plural': 'проекты'},
        ),
        migrations.AddField(
            model_name='measurement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
