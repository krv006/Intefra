from django.contrib import admin
from django.contrib.admin import ModelAdmin
from mptt.admin import DraggableMPTTAdmin

from apps.models import Category, Product, Brand, Address


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    pass


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    pass


@admin.register(Brand)
class BrandModelAdmin(ModelAdmin):
    pass


@admin.register(Address)
class AddressModelAdmin(ModelAdmin):
    pass
