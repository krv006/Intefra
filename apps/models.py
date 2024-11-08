from django.db.models import Model, PositiveIntegerField, ForeignKey, CASCADE, EmailField, ImageField, TextChoices, \
    CharField, SmallIntegerField, BooleanField, URLField
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
    category = ForeignKey('apps.Category', CASCADE, related_name='products')

    # TODO discount_price mana shuni kiritganda nechi foiz sale boletganini xam chiqazib berishi kerak -> ustozdan sorimiz
    # TODO sale nechi foiz kiritganda shunda summasini ozi aftamatik olishi kerak -> ustozdan sorimiz


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
