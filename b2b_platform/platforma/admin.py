from django.contrib import admin
from . import models


# Интерфейс администратора
class CustomerAdmin (admin.ModelAdmin):
    fields = ('title',
              ('inn', 'kpp'),
              ('legal_address', 'actual_address'),
              ('name', 'phone'))
    # readonly_fields = ('title', 'inn', 'kpp', 'legal_address', 'actual_address', 'name', 'phone')


class ProducerAdmin (admin.ModelAdmin):
    fields = ('title',
              ('inn', 'kpp'),
              ('legal_address', 'actual_address'),
              ('name', 'phone'))
    # readonly_fields = ('title', 'inn', 'kpp', 'legal_address', 'actual_address', 'name', 'phone')


class CategoryAdmin (admin.ModelAdmin):
    pass


class TenderAdmin (admin.ModelAdmin):
    fields = ('customer',
              'title',
              ('city_tender', 'category'),
              ('placement_date', 'last_modified_date'),
              ('expiration_date', 'budget_tender'),
              'requirement',
              'description',
              'file_tender')
    readonly_fields = ('placement_date', 'last_modified_date')


class OfferAdmin (admin.ModelAdmin):
    fields = ('title',
              'producer',
              'customer',
              'price_offer',
              ('placement_date', 'last_modified_date'),
              'description',
              'file_offer')
    readonly_fields = ('placement_date', 'last_modified_date')


# Register your models here.
admin.site.register (models.Customer, CustomerAdmin)
admin.site.register (models.Producer, ProducerAdmin)
admin.site.register (models.Category, CategoryAdmin)
admin.site.register (models.Order, TenderAdmin)
admin.site.register (models.Offer, OfferAdmin)
