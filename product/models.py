from django.db import models

# Create your models here.
Shirt_Type = [('FORMAL','formal'),('CASUAL','casual'),('HOODIE','hoodie')]
Pant_Type = [('FORMAL','formal'),('CASUAL','casual'),('JEANS','jeans')]
Shoe_Type = [('FORMAL','formal'),('CANVAS','canvas'),('LOFER','lofer'),('SNEAKERS','sneakers')]
Status = [('REGULAR','regular'),('TREND','trend'),('TODAYS DEAL','todays deal')]
class Shirt(models.Model):
    name=models.CharField(max_length=40)
    shirt_type=models.CharField(max_length=10,choices=Shirt_Type)
    price=models.IntegerField()
    discount=models.IntegerField()
    image=models.ImageField(upload_to='shirt_photo')
    status=models.CharField(max_length=12,choices=Status)
    description=models.TextField(default='',blank=True)

    def get_shirt_data(self,shirt_ids):
        shirt = Shirt.objects.filter(id__in=shirt_ids)
        return shirt
    
class Pant(models.Model):
    name=models.CharField(max_length=40)
    pant_type=models.CharField(max_length=10,choices=Pant_Type)
    price=models.IntegerField()
    discount=models.IntegerField()
    image=models.ImageField(upload_to='pant_photo')
    status=models.CharField(max_length=12,choices=Status)
    description=models.TextField(default='',blank=True)

    def get_pant_data(self,pant_ids):
        pant = Pant.objects.filter(id__in=pant_ids)
        return pant

class Shoe(models.Model):
    name=models.CharField(max_length=40)
    shoe_type=models.CharField(max_length=10,choices=Shoe_Type)
    price=models.IntegerField()
    discount=models.IntegerField()
    image=models.ImageField(upload_to='shoe_photo')
    status=models.CharField(max_length=12,choices=Status)
    description=models.TextField(default='',blank=True)

    def get_shoe_data(self,shoe_ids):
        shoe = Shoe.objects.filter(id__in=shoe_ids)
        return shoe