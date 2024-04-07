# Generated by Django 4.1.7 on 2023-02-25 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_publication_photo_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Фото 1'),
        ),
        migrations.AddField(
            model_name='publication',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Фото 2'),
        ),
        migrations.AddField(
            model_name='publication',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Фото 3'),
        ),
        migrations.AddField(
            model_name='publication',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Фото 4'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]