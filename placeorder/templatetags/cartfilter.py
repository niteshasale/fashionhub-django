from django import template
from product.models import Shirt,Pant,Shoe
from placeorder.models import PlaceOrder

register = template.Library()
@register.filter(name="create_id")
def create_id(pro,second):
    return str(pro.id) + second
    print(str(pro.id) + second)

@register.filter(name="product_price")
def product_price(pro):
    pro = pro.price-pro.discount/100*pro.price
    return '₹'+str(int(pro))


@register.filter(name="create_counter")
def create_counter(data):
    return int(data)


@register.filter(name="shirt_total")
def shirt_total(pro,cart):
    val = pro.price-pro.discount/100*pro.price 
    quan = cart['Shirt'][str(pro.id)]
    return str(quan) + 'x'+ '='+ ' '+str(int(val)*int(quan))

@register.filter(name="pant_total")
def pant_total(pro,cart):
    val = pro.price-pro.discount/100*pro.price 
    quan = cart['Pant'][str(pro.id)]
    return str(quan) + 'x'+ '='+ ' '+str(int(val)*int(quan))

@register.filter(name="shoe_total")
def shoe_total(pro,cart):
    val = pro.price-pro.discount/100*pro.price 
    quan = cart['Shoe'][str(pro.id)]
    return str(quan) + 'x'+ '='+ ' '+str(int(val)*int(quan))


@register.filter(name="total_amount")
def total_amount(cart):
    all_total = 0
    for i in cart:
        if i == 'Shirt':
            for key,quan in cart['Shirt'].items():
                key = int(key)
                quan = int(quan)
                pro = Shirt.objects.get(id=key)
                val = pro.price-pro.discount/100*pro.price
                val = int(val)
                all_total = all_total + val*quan
        elif i == 'Pant':
            for key,quan in cart['Pant'].items():
                key = int(key)
                quan = int(quan)
                pro = Pant.objects.get(id=key)
                val = pro.price-pro.discount/100*pro.price
                val = int(val)
                all_total = all_total + val*quan
        else:
            for key,quan in cart['Shoe'].items():
                key = int(key)
                quan = int(quan)
                pro = Shoe.objects.get(id=key)
                val = pro.price-pro.discount/100*pro.price
                val = int(val)
                all_total = all_total + val*quan
        
    return '₹'+str(int(all_total))    

@register.filter(name="get_image_orderlist")
def get_image_orderlist(pro):
    data = PlaceOrder.objects.get(id=pro.id)
    try:
        if type(data.shirt_id_id) == int:
            shirt_data = Shirt.objects.get(id=data.shirt_id_id)
            return shirt_data.image.url
        elif type(data.pant_id_id) == int:
            pant_data = Pant.objects.get(id=data.pant_id_id)
            return pant_data.image.url
        elif type(data.shoe_id_id) == int:
            shoe_data = Shoe.objects.get(id=data.shoe_id_id)
            return shoe_data.image.url
        else:
            return 
    except:
        pass                    
@register.filter(name="get_name_orderlist")
def get_name_orderlist(pro):
    data = PlaceOrder.objects.get(id=pro.id)
    try:
        if type(data.shirt_id_id) == int:
            shirt_data = Shirt.objects.get(id=data.shirt_id_id)
            return shirt_data.name
        elif type(data.pant_id_id) == int:
            pant_data = Pant.objects.get(id=data.pant_id_id)
            return pant_data.name
        elif type(data.shoe_id_id) == int:
            shoe_data = Shoe.objects.get(id=data.shoe_id_id)
            return shoe_data.name
        else:
            return 
    except:
        pass     