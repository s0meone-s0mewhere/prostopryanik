# Generated by Django 4.1.7 on 2024-01-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_publication_conviviality_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prices',
            name='rolls_price',
            field=models.CharField(default=1, max_length=20, verbose_name='Цена рулетов'),
            preserve_default=False,
        ),
    ]