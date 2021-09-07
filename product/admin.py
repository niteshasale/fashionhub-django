from django.contrib import admin
from .models import Shirt,Pant,Shoe
# Register your models here.
@admin.register(Shirt)
class ShirtAdmin(admin.ModelAdmin):
    list_display=('name','shirt_type','price','discount','image','status','description')

@admin.register(Pant)
class PantAdmin(admin.ModelAdmin):
    list_display=('name','pant_type','price','discount','image','status','description')

@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display=('name','shoe_type','price','discount','image','status','description')

