from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Shirt,Pant,Shoe
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def quantity(request):
    if request.method =='POST':
        count = 0
        cart = request.session.get('cart')
        print(request.session['cart'])
        for i in cart:
            for j in cart[i]:
                count = count + 1
        return HttpResponse(count)
def homecart(request):
    if request.method =='POST':
        result = ''
        count = 0
        demo = request.POST.get('product_id')
        product_id,model_name = demo.split(',')
        cart = request.session.get('cart')
        if cart:
            if model_name in cart:
                if product_id in cart[model_name]:
                    del cart[model_name][product_id]
                    result = 'Add To Cart'
                else:
                    cart[model_name][product_id] = 1
                    result = 'Remove'
            else:
                cart[model_name] = {}
                cart[model_name][product_id] = 1
                result = 'Remove'
        else:
            cart = {}
            cart[model_name] = {}
            cart[model_name][product_id] = 1
            result = 'Remove'  

        request.session['cart'] = cart
        print(request.session['cart'])
        for i in cart:
            for j in cart[i]:
                count = count + 1
        com = result + str(count)                
        return HttpResponse(com)
        
      
    
def home(request):
    shirt_t = Shirt.objects.filter(status="TREND")
    pant_t = Pant.objects.filter(status="TREND")
    shoe_t = Shoe.objects.filter(status="TREND")
    
    shirt_d = Shirt.objects.filter(status="TODAYS DEAL")
    pant_d = Pant.objects.filter(status="TODAYS DEAL")
    shoe_d = Shoe.objects.filter(status="TODAYS DEAL")

    value = {}
    value['shirt_t']=shirt_t
    value['pant_t']=pant_t
    value['shoe_t']=shoe_t
    value['shirt_d']=shirt_d
    value['pant_d']=pant_d
    value['shoe_d']=shoe_d
    print(request.session.get('user_id'))
    print(request.session.get('user_email'))
    return render(request,'product/home.html',value)

def shirt(request,data):
    if data == 'ALL':
        value = Shirt.objects.all()
        paginator = Paginator(value,9)
        page=request.GET.get('page')
        page_no = Paginator.get_page(paginator,page)
    else:
        value = Shirt.objects.filter(shirt_type=data)
        paginator = Paginator(value,9)
        page=request.GET.get('page')
        page_no = Paginator.get_page(paginator,page)        
    return render(request,'product/shirt.html',{'data':data,'value':value,'page_no':page_no})

def pant(request,data):
    if data == 'ALL':
        value = Pant.objects.all()
        paginator = Paginator(value,9)
        page=request.GET.get('page')
        page_no = Paginator.get_page(paginator,page)
    else:
        value = Pant.objects.filter(pant_type=data)
        paginator = Paginator(value,9)
        page=request.GET.get('page')
        page_no = Paginator.get_page(paginator,page)    
    return render(request,'product/pant.html',{'data':data,'value':value,'page_no':page_no})

def shoe(request,data):
    if data =='ALL':
        value = Shoe.objects.all()
        paginator = Paginator(value,9)
        page=request.GET.get('page')
        page_no = Paginator.get_page(paginator,page)
    else:
        value = Shoe.objects.filter(shoe_type=data)
        paginator = Paginator(value,9)
        page=request.GET.get('page')
        page_no = Paginator.get_page(paginator,page)    
    return render(request,'product/shoe.html',{'data':data,'value':value,'page_no':page_no})

