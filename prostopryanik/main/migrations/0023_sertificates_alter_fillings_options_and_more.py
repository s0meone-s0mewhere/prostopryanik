# Generated by Django 4.1.7 on 2024-01-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_publication_photo3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sertificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='sertificates/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Сертификат',
                'verbose_name_plural': 'Сертификаты',
            },
        ),
        migrations.AlterModelOptions(
            name='fillings',
            options={'ordering': ['-date_and_time'], 'verbose_name': 'Начинка', 'verbose_name_plural': 'Начинки'},
        ),
        migrations.AlterModelOptions(
            name='prices',
            options={'verbose_name': 'Цена', 'verbose_name_plural': 'Цены'},
        ),
    ]
