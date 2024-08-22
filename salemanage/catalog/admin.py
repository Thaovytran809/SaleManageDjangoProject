from django.contrib import admin
from .models import Catagory, Product, Customer, Order  
# Register your models here.

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('c_name', 'c_image')
admin.site.register(Catagory, CatagoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('p_name', 'catagory', 'price', 'p_image')
admin.site.register(Product, ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cus_name', 'pkkh')
admin.site.register(Customer, CustomerAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'catagory', 'product', 'count', 'total')
admin.site.register(Order, OrderAdmin)
