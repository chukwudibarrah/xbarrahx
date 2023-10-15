from django.contrib import admin
from . models import ProductModel

# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'date_created')


admin.site.register(ProductModel, ProductModelAdmin)