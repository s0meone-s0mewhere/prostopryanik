from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from . import models


LIST_OF_CATEGORIES_RU = [
    'Торт',
    'Торт без сахара и без глютена',
    'Бенто-торт',
    'Бенто-торт без сахара и без глютена',
    'Капкейки',
    'Капкейки без сахара и без глютена',
    'Рулеты',
    'Леденцы',
    'Пряники',
    'Конфеты',
    'Кейк попсы',
    'Мармелад'
]

LIST_OF_CATEGORIES = [
    'classic_cakes', 
    'cakes_for_diabetics', 
    'bentoo_cakes', 
    'bentoo_cakes_for_diabetics', 
    'cupcakes', 
    'cupcakes_for_diabetics', 
    'rolls', 
    'sugar_lollipops', 
    'painted_gingerbread', 
    'chocolate_sweets', 
    'cake_pops', 
    'marmelade_candies'
]

prices = models.Prices.objects.get(pk=1) 

LIST_OF_PRICES = [
    prices.classic_cakes_price, 
    prices.cakes_for_diabetics_price, 
    prices.bentoo_cakes_price, 
    prices.bentoo_cakes_for_diabetics_price, 
    prices.cupcakes_price, 
    prices.cupcakes_for_diabetics_price, 
    prices.rolls_price, 
    prices.sugar_lollipops_price, 
    prices.painted_gingerbread_price, 
    prices.chocolate_sweets_price, 
    prices.cake_pops_price, 
    prices.marmelade_candies_price
]

MIN_COUNTS = [
    'Минимальный вес торта для заказа: 1,5кг', 
    'Минимальный вес торта для заказа: 1,5кг', 
    'Минимальный вес торта для заказа: 500г',
    'Минимальный вес торта для заказа: 500г', 
    'Минимальное количество штук в одном заказе: 6', 
    'Минимальное количество штук в одном заказе: 6', 
    'Минимальное количество штук в одном заказе: 1', 
    'Минимальное количество штук в одном заказе: 20', 
    'Минимальное количество штук в одном заказе: 5', 
    'Минимальное количество штук в одном заказе: 15', 
    'Минимальное количество штук в одном заказе: 8', 
    'Минимальное количество штук в одном заказе: 20'
]

class MainPage(ListView):
    model = models.Publication
    template_name = 'main/index.html'
    context_object_name = 'puplications'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publications'] = models.Publication.objects.all()[:3]
        context['list_of_categories'] = LIST_OF_CATEGORIES
        context['list_of_categories_ru'] = LIST_OF_CATEGORIES_RU
        context['list_of_prices'] = LIST_OF_PRICES
        context['min_counts'] = MIN_COUNTS
        context['certificates'] = models.Certificates.objects.all()[:3]
        context['fillings'] = models.Fillings.objects.all()
        context['festive_cakes'] = models.Publication.objects.filter(is_conviviality=True)
        context['button'] = True
        context['not_cakes'] = models.Publication.objects.exclude(category='bentoo_cakes_for_diabetics').exclude(category='bentoo_cakes').exclude(category='cakes_for_diabetics').exclude(category='classic_cakes')
        context['flowers'] = models.FlowersForCakes.objects.all()[:3]
        return context


def get_context(category):
    context = {}
    context['prices'] = prices
    context['list_of_categories'] = LIST_OF_CATEGORIES
    context['list_of_categories_ru'] = LIST_OF_CATEGORIES_RU
    context['list_of_prices'] = LIST_OF_PRICES
    context['min_counts'] = MIN_COUNTS
    context['publications'] = models.Publication.objects.filter(category=category) 
    context['button'] = True
    return context


class AllPublications(ListView):
    paginate_by = 24
    model = models.Publication
    template_name = 'main/all_publications.html'
    context_object_name = 'publications'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_of_categories'] = LIST_OF_CATEGORIES
        context['list_of_categories_ru'] = LIST_OF_CATEGORIES_RU
        context['list_of_prices'] = LIST_OF_PRICES
        context['min_counts'] = MIN_COUNTS
        context['button'] = True
        return context


def publication_page(request, slug_for_publication):
    context = {}
    context['prices'] = prices
    context['list_of_categories'] = LIST_OF_CATEGORIES
    context['list_of_categories_ru'] = LIST_OF_CATEGORIES_RU
    context['list_of_prices'] = LIST_OF_PRICES
    context['min_counts'] = MIN_COUNTS
    context['publication'] = get_object_or_404(models.Publication, slug=slug_for_publication)
    return render(request, 'main/publication.html', context) 

def classic_cakes(request):
    return render(request, 'main/classic_cakes.html', get_context('classic_cakes'))

def cakes_for_diabetics(request):
    return render(request, 'main/cakes_for_diabetics.html', get_context('cakes_for_diabetics'))

def bentoo_cakes(request):
    return render(request, 'main/bentoo_cakes.html', get_context('bentoo_cakes'))

def bentoo_cakes_for_diabetics(request):
    return render(request, 'main/bentoo_cakes_for_diabetics.html', get_context('bentoo_cakes_for_diabetics'))

def cupcakes(request):
    return render(request, 'main/cupcakes.html', get_context('cupcakes'))

def cupcakes_for_diabetics(request):
    return render(request, 'main/cupcakes_for_diabetics.html', get_context('cupcakes_for_diabetics'))

def rolls(request):
    return render(request, 'main/rolls.html', get_context('rolls'))

def sugar_lollipops(request):
    return render(request, 'main/sugar_lollipops.html', get_context('sugar_lollipops'))

def painted_gingerbread(request):
    return render(request, 'main/painted_gingerbread.html', get_context('painted_gingerbread'))

def chocolate_sweets(request):
    return render(request, 'main/chocolate_sweets.html', get_context('chocolate_sweets'))

def cake_pops(request):
    return render(request, 'main/cake_pops.html', get_context('cake_pops'))

def marmelade_candies(request):
    return render(request, 'main/marmelade_candies.html', get_context('marmelade_candies'))

def certificates(request):
    context = {}
    context['certificates'] = models.Certificates.objects.all()
    context['button'] = False
    return render(request, 'main/certificates.html', context=context)

def flowers_for_cakes(request):
    context = {}
    context['flowers'] = models.FlowersForCakes.objects.all()
    context['button'] = False
    return render(request, 'main/flowers_for_cakes.html', context=context)