from django.db import models
from django.urls import reverse


class Publication(models.Model):
    class Kinds(models.TextChoices):
        BENTOO_CAKES_FOR_DIABETICS = 'bentoo_cakes_for_diabetics', 'Бенто торты для диабетиков'
        BENTOO_CAKES = 'bentoo_cakes', 'Бенто торты'
        CAKE_POPS = 'cake_pops', 'Кейк попсы'
        CAKES_FOR_DIABETICS = 'cakes_for_diabetics', 'Торты для диабетиков'
        CHOCOLATE_SWEETS = 'chocolate_sweets', 'Шоколад и конфеты'
        CLASSIC_CAKES = 'classic_cakes', 'Классические торты'
        CUPCAKES_FOR_DIABETICS = 'cupcakes_for_diabetics', 'Капкейки для диабетиков'
        CUPCAKES = 'cupcakes', 'Капкейки'
        ROLLS = 'rolls', 'Рулеты'
        MARMELADE_CANDIES = 'marmelade_candies', 'Мармеладные конфеты'
        PAINTED_GINGERBREAD = 'painted_gingerbread', 'Расписные пряники'
        SUGAR_LOLLIPOPS = 'sugar_lollipops', 'Леденцы из сахара'


    title = models.CharField(max_length=70, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=70, choices=Kinds.choices, verbose_name='Категория')
    publication_time = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата и время публикации')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    photo1 = models.ImageField(upload_to='publications/%Y/%B/', default='plug.jpg', verbose_name='Фото 1')
    photo2 = models.ImageField(upload_to='publications/%Y/%B/', default='plug.jpg', verbose_name='Фото 2')
    photo3 = models.ImageField(upload_to='publications/%Y/%B/', null=True, blank=True, default='plug.jpg', verbose_name='Фото 3')
    photo4 = models.ImageField(upload_to='publications/%Y/%B/', null=True, blank=True, default='plug.jpg', verbose_name='Фото 4')
    is_conviviality = models.BooleanField(default=False, verbose_name='Праздничный торт')
    
    
    def get_absolute_url(self):
        return reverse('publication_page', kwargs={'slug_for_publication': self.slug})

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'
        ordering = ['-publication_time']


class Prices(models.Model):
    bentoo_cakes_for_diabetics_price = models.CharField(max_length=20, verbose_name='Цена бенто тортов без сахара')
    bentoo_cakes_price = models.CharField(max_length=20, verbose_name='Цена бенто тортов')
    cake_pops_price = models.CharField(max_length=20, verbose_name='Цена кейк попсов')
    cakes_for_diabetics_price = models.CharField(max_length=20, verbose_name='Цена тортов без сахара')
    chocolate_sweets_price = models.CharField(max_length=20, verbose_name='Цена шоколадных конфет')
    classic_cakes_price = models.CharField(max_length=20, verbose_name='Цена классических тортов')
    cupcakes_for_diabetics_price = models.CharField(max_length=20, verbose_name='Цена капкейков без сахара')
    cupcakes_price = models.CharField(max_length=20, verbose_name='Цена капкейков')
    marmelade_candies_price = models.CharField(max_length=20, verbose_name='Цена мармелада')
    painted_gingerbread_price = models.CharField(max_length=20, verbose_name='Цена расписных пряников')
    sugar_lollipops_price = models.CharField(max_length=20, verbose_name='Цена леденцов из сахара')
    rolls_price = models.CharField(max_length=20, verbose_name='Цена рулетов')


    class Meta:
        verbose_name_plural = 'Цены'
        verbose_name = 'Цена'


class Fillings(models.Model):
    title = models.CharField(max_length=70, verbose_name='Название')
    description = models.TextField(max_length=250, verbose_name='Описание')
    photo = models.ImageField(upload_to='fillings/%Y/%B/', default='plug.jpg', verbose_name='Фото 1')
    date_and_time = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата и время публикации')


    class Meta:
        verbose_name_plural = 'Начинки'
        verbose_name = 'Начинка'
        ordering = ['-date_and_time']


class Certificates(models.Model):
    photo = models.ImageField(upload_to='certificates/', verbose_name='Фото')

    class Meta:
        verbose_name_plural = 'Сертификаты'
        verbose_name = 'Сертификат'

class FlowersForCakes(models.Model):
    photo = models.ImageField(upload_to='flowers_for_cakes/', verbose_name='Фото')

    class Meta:
        verbose_name_plural = 'Цветы на торт'
        verbose_name = 'Цветок на торт'

