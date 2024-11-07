from django.db.models import Model, PositiveIntegerField, ForeignKey, CASCADE, EmailField, ImageField, TextChoices, \
    CharField
from django_ckeditor_5.fields import CKEditor5Field
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = CharField(max_length=255)
    parent = TreeForeignKey('self', CASCADE, null=True, blank=True, related_name='children')
    background_image = ImageField(upload_to='categories/')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(Model):
    class Size(TextChoices):
        F50 = '50', '50'
        F52 = '52', '52'
        F54 = '54', '54'
        F56 = '56', '56'

    name = CharField(max_length=255)
    price = PositiveIntegerField(default=0)
    description = CKEditor5Field()
    sale = PositiveIntegerField(default=0)
    size = CharField(max_length=2, choices=Size.choices, default=Size.F50)
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


class Image(Model):
    image = ImageField(upload_to='images/')
    product = ForeignKey('apps.Product', on_delete=CASCADE, related_name='images')
