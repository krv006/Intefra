from django.db.models import Model, PositiveIntegerField, ForeignKey, CASCADE, EmailField, ImageField
from django.forms import CharField
from django_ckeditor_5.fields import CKEditor5Field


class Category(Model):
    name = CharField(max_length=255)


class Product(Model):
    name = CharField(max_length=255)
    price = PositiveIntegerField(db_default=0)
    description = CKEditor5Field()
    category = ForeignKey('apps.Category', CASCADE, related_name='products')


class Address(Model):
    name = CharField(max_length=255)
    surname = CharField(max_length=255)
    city = CharField(max_length=255)
    email = EmailField()
    home_number = PositiveIntegerField(db_default=0)
    phone_number = CharField(max_length=255)
    description = CKEditor5Field()


class Brand(Model):
    image = ImageField(upload_to='images/brand/')
