from django.db import models
from product.models import Shirt,Pant,Shoe
from account.models import User
import datetime
# Create your models here.


class PlaceOrder(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    shirt_id = models.ForeignKey(Shirt,on_delete=models.CASCADE,blank=True)
    pant_id = models.ForeignKey(Pant,on_delete=models.CASCADE,blank=True)
    shoe_id = models.ForeignKey(Shoe,on_delete=models.CASCADE,blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    
    