"""prostopryanik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.sitemaps.views import sitemap
from django.urls import path
from . import views
from .sitemaps import PublicationsSitemap, StaticViewSitmap

sitemaps = {
    'publications': PublicationsSitemap, # sitemap for Publication model
    'static': StaticViewSitmap # sitemap for static pages
}

urlpatterns = [
    path('all_publications', views.AllPublications.as_view(), name='all_publications'),
    path('publications/<str:slug_for_publication>', views.publication_page, name='publication_page'),
    path('', views.MainPage.as_view(), name='main'),
    path('classic_cakes', views.classic_cakes, name='classic_cakes'),
    path('cakes_for_diabetics', views.cakes_for_diabetics, name='cakes_for_diabetics'),
    path('bentoo_cakes', views.bentoo_cakes, name='bentoo_cakes'),
    path('bentoo_cakes_for_diabetics', views.bentoo_cakes_for_diabetics, name='bentoo_cakes_for_diabetics'),
    path('cupcakes', views.cupcakes, name='cupcakes'),
    path('cupcakes_for_diabetics', views.cupcakes_for_diabetics, name='cupcakes_for_diabetics'),
    path('rolls', views.rolls, name='rolls'),
    path('sugar_lollipops', views.sugar_lollipops, name='sugar_lollipops'),
    path('painted_gingerbread', views.painted_gingerbread, name='painted_gingerbread'),
    path('chocolate_sweets', views.chocolate_sweets, name='chocolate_sweets'),
    path('cake_pops', views.cake_pops, name='cake_pops'),
    path('marmelade_candies', views.marmelade_candies, name='marmelade_candies'),
    path('certificates', views.certificates, name='certificates'),
    path('flowers_for_cakes', views.flowers_for_cakes, name='flowers_for_cakes'),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    )
]
