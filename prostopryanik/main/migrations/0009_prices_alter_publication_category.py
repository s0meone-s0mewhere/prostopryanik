# Generated by Django 4.1.7 on 2023-02-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_publication_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bentoo_cakes_for_diabetics_price', models.CharField(max_length=20, verbose_name='Цена бенто тортов без сахара')),
                ('bentoo_cakes_price', models.CharField(max_length=20, verbose_name='Цена бенто тортов')),
                ('cake_pops_price', models.CharField(max_length=20, verbose_name='Цена кейк попсов')),
                ('cakes_for_diabetics_price', models.CharField(max_length=20, verbose_name='Цена тортов без сахара')),
                ('chocolate_sweets_price', models.CharField(max_length=20, verbose_name='Цена шоколадных конфет')),
                ('classic_cakes_price', models.CharField(max_length=20, verbose_name='Цена классических тортов')),
                ('cupcakes_for_diabetics_price', models.CharField(max_length=20, verbose_name='Цена капкейков без сахара')),
                ('cupcakes_price', models.CharField(max_length=20, verbose_name='Цена капкейков')),
                ('isomalt_lollipops_price', models.CharField(max_length=20, verbose_name='Цена леденцов из изомальта')),
                ('marmelade_candies_price', models.CharField(max_length=20, verbose_name='Цена мармелада')),
                ('painted_gingerbread_price', models.CharField(max_length=20, verbose_name='Цена расписных пряников')),
                ('sugar_lollipops_price', models.CharField(max_length=20, verbose_name='Цена леденцов из сахара')),
            ],
            options={
                'verbose_name': 'Цены',
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('bentoo_cakes_for_diabetics', 'Бенто торты для диабетиков'), ('bentoo_cakes', 'Бенто торты'), ('cake_pops', 'Кейк попсы'), ('cakes_for_diabetics', 'Торты для диабетиков'), ('chocolate_sweets', 'Шоколад и конфеты'), ('classic_cakes', 'Классические торты'), ('cupcakes_for_diabetics', 'Капкейки для диабетиков'), ('cupcakes', 'Капкейки'), ('isomalt_lollipops', 'Леденцы из изомальта'), ('marmelade_candies', 'Мармеладные конфеты'), ('painted_gingerbread', 'Расписные пряники'), ('sugar_lollipops', 'Леденцы из сахара')], max_length=70, verbose_name='Категория'),
        ),
    ]
