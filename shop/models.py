from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

class Product(models.Model):

    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True)
    digital = models.BooleanField(default=False)
    image = models.ImageField(null=True)
    slug = models.SlugField(unique=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubric')
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
        ordering = 'name',

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"slug": self.slug})

class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

class OrderItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

class Rubric(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='name')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Rubrics'
        verbose_name = 'Rubric'
        ordering = ['name']