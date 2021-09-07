from django import template
from product.models import Shirt,Pant,Shoe

register = template.Library()
@register.filter(name="product_price")
def product_price(pro):
    pro = pro.price-pro.discount/100*pro.price
    return '₹'+str(int(pro))

@register.filter(name='size')
def shirt_size(pro,s): # s means all shirt size size_m size_l size_xl direct pass (quantity check)
    if s>1:
        return True
@register.filter(name="style")
def style(data,d):
    if  data==d:
        return True
