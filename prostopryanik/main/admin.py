from django.contrib import admin
from .models import Publication, Prices, Fillings, Certificates, FlowersForCakes


# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_time', 'category', 'slug', 'price', 'is_conviviality')
    list_display_links = ('title', 'price', 'is_conviviality')
    search_fields = ('title', 'description', 'category', 'slug', 'category')
    prepopulated_fields = {"slug": ("title",)}


class FillingsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)


admin.site.register(Publication, PublicationAdmin)
admin.site.register(Prices)
admin.site.register(Fillings, FillingsAdmin)
admin.site.register(Certificates)
admin.site.register(FlowersForCakes)
