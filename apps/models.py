from django.db.models import Model, PositiveIntegerField, ForeignKey, CASCADE, EmailField, ImageField, TextChoices, \
    CharField, SmallIntegerField, BooleanField, URLField, TextField
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

    class Poll(TextChoices):
        MALE = 'Male', 'male'
        FEMALE = 'Female', 'female'

    name = CharField(max_length=255)
    price = PositiveIntegerField(default=0)
    description = CKEditor5Field()
    discount_price = SmallIntegerField(default=0, null=True, blank=True)
    size = CharField(max_length=2, choices=Size.choices, default=Size.F50)
    poll = CharField(max_length=10, choices=Poll.choices, default=Poll.MALE)
    material = CharField(max_length=255, null=True, blank=True)
    lining = CharField(max_length=255, null=True, blank=True)  # todo podkladka
    made_from = CharField(max_length=255, null=True, blank=True)
    category = ForeignKey('apps.Category', CASCADE, related_name='products')

    # TODO discount_price mana shuni kiritganda nechi foiz sale boletganini xam chiqazib berishi kerak -> ustozdan sorimiz
    # TODO sale nechi foiz kiritganda shunda summasini ozi aftamatik olishi kerak -> ustozdan sorimiz


class Address(Model):
    class Type(TextChoices):
        HOME = 'Доставка на дом', 'доставка на дом'
        FILIAL = 'Пункт выдачи СДЭК', 'пункт выдачи СДЭК'
        RUSSIAN = 'Россия', 'pоссия'

    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    city = CharField(max_length=100)
    home_number = CharField(max_length=100)
    deliver_place = CharField(max_length=100, choices=Type.choices, default=Type.RUSSIAN)
    email = EmailField()
    phone_number = CharField(max_length=100)
    description = TextField()


class Brand(Model):
    image = ImageField(upload_to='images/brand/')


class Payment(Model):
    name = CharField(max_length=255)
    surname = CharField(max_length=255)
    delivery_home = BooleanField(default=True)
    SDEK_pickup_point = BooleanField(default=False)
    region = CharField(max_length=255)


class Image(Model):
    image = ImageField(upload_to='images/product/')
    product = ForeignKey('apps.Product', on_delete=CASCADE, related_name='images')


class SiteSettings(Model):
    instagram = URLField()
    telegram = URLField()


class QuickOrder(Model):
    name = CharField(max_length=255)
    description = TextField()
    price = PositiveIntegerField(null=True, blank=True, default=0)
    discount = PositiveIntegerField(null=True, blank=True, default=0)
    size = CharField(max_length=255, choices=Product.Size.choices, null=True, blank=True, db_default=Product.Size.F50)
