from django.contrib import admin
from .models import PlaceOrder
# Register your models here.

@admin.register(PlaceOrder)
class PlaceOrderAdmin(admin.ModelAdmin):
    list_display=('id','price','quantity','phone','address','city','state','zipcode')

