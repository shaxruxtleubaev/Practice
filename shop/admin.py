from django.contrib import admin
from shop.models import Product, Customer, OrderItem, Order, ShippingAddress, Rubric

class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'digital', 'published', )
    list_display_links = ('name',)

admin.site.register(Product, ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):

    list_display = ('user', 'name',)
    list_display_links = ('user',)

admin.site.register(Customer, CustomerAdmin)

class OrderAdmin(admin.ModelAdmin):

    list_display = ('customer', 'date_ordered', 'transaction_id', 'complete',)
    list_display_links = ('customer',)

admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):

    list_display = ('product', 'order', 'quantity', 'date_added')
    list_display_links = ('product',)

admin.site.register(OrderItem, OrderItemAdmin)

class ShippingAddressAdmin(admin.ModelAdmin):

    list_display = ('customer', 'order', 'date_added',)
    list_display_links = ('customer',)

admin.site.register(ShippingAddress, ShippingAddressAdmin)

class RubricAdmin(admin.ModelAdmin):

    list_display = ('name',)
    list_display_links = ('name',)

admin.site.register(Rubric, RubricAdmin)