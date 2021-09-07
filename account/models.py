from django.db import models
from product.models import Shirt

# Create your models here.
Gender = [('male','male'),('female','female')]
class User(models.Model):
    full_name = models.CharField(max_length=60)
    email = models.EmailField()
    mobile = models.DecimalField(max_digits=10, decimal_places=0)
    password = models.CharField(max_length=100)

    def Email_exits(self):
        if User.objects.filter(email=self.email):
            return True
        return False
    def Mobile_exist(self):
        if User.objects.filter(mobile=self.mobile):
            return True
        return False    
    
    def Login_check(self,email):
        try:
            user = User.objects.get(email=email)
            return user 
        except: 
            return False    

