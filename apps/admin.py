from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline
from mptt.admin import DraggableMPTTAdmin

from apps.models import Category, Product, Brand, Address, Image, SiteSettings, QuickOrder


class ImageProductStackedInline(StackedInline):
    model = Image
    extra = 1
    max_num = 5
    min_num = 1


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    pass


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    inlines = ImageProductStackedInline,


@admin.register(Brand)
class BrandModelAdmin(ModelAdmin):
    pass


@admin.register(Address)
class AddressModelAdmin(ModelAdmin):
    pass


@admin.register(SiteSettings)
class SiteSettingsModelAdmin(ModelAdmin):
    pass


@admin.register(QuickOrder)
class QuickOrderModelAdmin(ModelAdmin):
    pass
