from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *     # this models means these are in same app

class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('desc',)

admin.site.register(Customer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
