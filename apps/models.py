from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ImageField, CharField, TextField, ForeignKey, CASCADE, Model
from django.forms import ModelForm, BaseModelForm, FloatField, IntegerField, SlugField, EmailField
from django.utils.text import slugify


class BaseSlugModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class RegisterForm(ModelForm):
    name = CharField(50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Login(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Category(BaseSlugModel, BaseModelForm):
    image = ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Product(BaseSlugModel, BaseModelForm):
    description = TextField()
    price = FloatField()
    quantity = IntegerField()
    category_id = ForeignKey('apps.models', CASCADE(), related_name='products')

    def __str__(self):
        return self.name


class Order(BaseSlugModel, BaseModelForm):
    name = CharField(max_length=255)
    image = ImageField(upload_to='images/')
    price = FloatField()

    def __str__(self):
        return self.name

class Profile(BaseSlugModel, BaseModelForm):
    first_name = CharField(max_length=25)
    last_name = CharField(max_length=25)
    email = EmailField(unique=True)
    phone_number = CharField(max_length=13)
    mobile_number = CharField(max_length=14)
    skype = CharField(max_length=50)
    photo = ImageField(upload_to='images/')


class Product_update(BaseSlugModel, BaseModelForm):
    description = TextField()
    price = FloatField()
    quantity = IntegerField()
    category_id = ForeignKey('apps.models', CASCADE(), related_name='products')
    def __str__(self):
        return self.name
