# Generated by Django 4.1.7 on 2023-03-06 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_publication_photo4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fillings',
            name='title',
            field=models.CharField(max_length=70, verbose_name='Название'),
        ),
    ]