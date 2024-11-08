from django.db.models import Count
from django_filters import NumberFilter, CharFilter
from django_filters.rest_framework import FilterSet

from apps.models import Category, Product


class ProductFilter(FilterSet):
    category_name = CharFilter(field_name="category__name", lookup_expr='icontains')
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = 'category',


class CategoryFilter(FilterSet):
    n = NumberFilter(method='filter_by_product_count')

    class Meta:
        model = Category
        fields = 'name',

    def filter_by_product_count(self, queryset, field, value):
        return queryset.annotate(product__count=Count('products')).filter(product__count=value)
