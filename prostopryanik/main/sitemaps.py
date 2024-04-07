"""
Django sitemap framework docs: https://docs.djangoproject.com/en/4.2/ref/contrib/sitemaps/
Also used https://pocoz.gitbooks.io/django-v-primerah/content/rasshirenie-prilozheniya-blog/dobavlenie-sitemap.html
"""

from django.contrib.sitemaps import Sitemap
from .models import Publication
from django.urls import reverse


class PublicationsSitemap(Sitemap):
    changefreq = 'always'
    protocol = 'https'
    
    def items(self):
        return Publication.objects.all()
    

class StaticViewSitmap(Sitemap):
    changefreq = 'always'
    protocol = 'https'
    
    def items(self):
        items = [
            'all_publications', 
            'main',
            'classic_cakes', 
            'cakes_for_diabetics',
            'bentoo_cakes_for_diabetics', 
            'cupcakes_for_diabetics',
            'rolls',
            'sugar_lollipops',
            'painted_gingerbread',
            'chocolate_sweets',
            'cake_pops',
            'marmelade_candies',
            'certificates',
        ]
        return items
    
    def location(self, item):
        return reverse(item)
