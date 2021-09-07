from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('homecart/',views.homecart,name="homecart"),
    path('quantity/',views.quantity,name="quantity"),
    path('shirt/<str:data>/',views.shirt,name="shirt"),
    path('pant/<str:data>/',views.pant,name="pant"),
    path('shoe/<str:data>/',views.shoe,name="shoe"),
]
