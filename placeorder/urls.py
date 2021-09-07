from django.urls import path
from .import views
from .middlewares.auth import auth_middleware
urlpatterns = [
    path('cart/',views.cartdetail,name='cart'),
    path('quantityupdate/',views.quantityupdate,name="quantityupdate"),
    path('checkout/',auth_middleware(views.checkout),name="checkout"),
    path('orderlist/',auth_middleware(views.orderlist),name="orderlist"),
]
