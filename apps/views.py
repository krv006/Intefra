from ctypes.wintypes import tagMSG

from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView

from apps.models import Category, Product
from apps.serializers import CategoryModelSerializer, ProductListModelSerializer


@extend_schema(tags=['category'])
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


@extend_schema(tags=['product'])
@extend_schema(description='product')
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListModelSerializer
    ordering = 'price',
    # TODO mana shu yerda created_at di qoshsa eng yangi eng eski -created_at shunaqa qilish kerak boaldi
    search_fields = 'name', 'description',
