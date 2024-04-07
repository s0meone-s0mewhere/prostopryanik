# Generated by Django 4.1.7 on 2023-02-25 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_publication_category_alter_publication_photo1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('bentoo_cakes_for_diabetics', 'Бенто торты для диабетиков'), ('bentoo_cakes', 'Бенто торты'), ('cake_pops', 'Кейк попсы'), ('cakes_for_diabetiks', 'Торты для диабетиков'), ('chocolate_sweets', 'Шоколад и конфеты'), ('classic_cakes', 'Классические торты'), ('cupcakes_for_diabetics', 'Капкейки для диабетиков'), ('cupcakes', 'Капкейки'), ('isomalt_lollipops', 'Леденцы из изомальта'), ('marmelade_candies', 'Мармеладные конфеты'), ('painted_gingerbread', 'Расписные пряники'), ('sugar_lollipops', 'Леденцы из сахара')], max_length=70, verbose_name='Категория'),
        ),
    ]