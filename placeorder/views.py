from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from product.models import Shirt,Pant,Shoe
from .forms import OrderRegistration
from .models import PlaceOrder
from account.models import User
# Create your views here.
def checkout(request):
    if request.method == 'POST':
        cart = request.session.get('cart')
        userid = request.session.get('user_id')
        user_id = User.objects.get(pk=userid)
        print(user_id)
        form = OrderRegistration(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            for i in cart:
                if i == 'Shirt':
                    for key,quan in cart['Shirt'].items():
                        pro = Shirt.objects.get(pk=key)
                        val = pro.price-pro.discount/100*pro.price
                        price = int(val)*quan
                        order = PlaceOrder(user_id=user_id,shirt_id=pro,price=price,quantity=quan,phone=phone,address=address,city=city,state=state,zipcode=zipcode)
                        order.save()
                      
                elif i == 'Pant':
                    for key,quan in cart['Pant'].items():
                        pro = Pant.objects.get(pk=key)
                        val = pro.price-pro.discount/100*pro.price
                        price = int(val)*quan
                        order = PlaceOrder(user_id=user_id,pant_id=pro,price=price,quantity=quan,phone=phone,address=address,city=city,state=state,zipcode=zipcode)
                        order.save()
                        
                else:
                    for key,quan in cart['Shoe'].items():
                        pro = Shoe.objects.get(pk=key)
                        val = pro.price-pro.discount/100*pro.price
                        price = int(val)*quan
                        order = PlaceOrder(user_id=user_id,shoe_id=pro,price=price,quantity=quan,phone=phone,address=address,city=city,state=state,zipcode=zipcode)
                        order.save()
            request.session['cart'] = {}
            return redirect('/placeorder/orderlist')                    


    else:
        form = OrderRegistration()
    return render(request,'placeorder/orders.html',{'form':form})



def orderlist(request):
    userid = request.session.get('user_id')
    pro = PlaceOrder.objects.filter(user_id=userid).order_by('-id')
       
    return render(request,'placeorder/orderlist.html',{'orders':pro})








def quantityupdate(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        model_name = request.POST['model_name']
        quan = request.POST['quan']
        print(product_id,model_name,quan)
        cart = request.session.get('cart')
        if cart:
            if quan == 0:
                cart[model_name][product_id] = 1
            else:
                cart[model_name][product_id]=int(quan)
        request.session['cart'] = cart
        print(request.session['cart'])    
        return HttpResponse('')

def cartdetail(request):
    value = {}
    cart = request.session.get('cart')
    if cart:
        for i in cart:
            if 'Shirt' == i:
                shirt_ids = []
                for j in cart[i]:
                    shirt_ids.append(j)
                shirt = Shirt()
                shirt_data = shirt.get_shirt_data(shirt_ids)
                value['shirt_data'] = shirt_data
            
            if 'Pant' == i:
                pant_ids = []
                for j in cart[i]:
                    pant_ids.append(j)
                pant = Pant()
                pantdata = pant.get_pant_data(pant_ids)
                value['pant_data'] = pantdata
                    
            if 'Shoe' == i:
                shoe_ids = []
                for j in cart[i]:
                    shoe_ids.append(j)
                shoe = Shoe()
                shoedata = shoe.get_shoe_data(shoe_ids)
                value['shoe_data'] = shoedata
    else:
        pass    
    return render(request,'placeorder/cartdetail.html',value)