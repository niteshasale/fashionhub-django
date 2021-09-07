from django.shortcuts import render,redirect
from .models import User
from .forms import UserRegistration,UserLogin
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
# Create your views here.

def registration(request):
    email_error = ''
    if request.method=='POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            pas = form.cleaned_data['password']
            password = make_password(pas)

            user = User(full_name=full_name,email=email,mobile=mobile,password=password)
            email_exist = user.Email_exits()
            mobile_exist = user.Mobile_exist()
            if email_exist:
                email_error = 'Email has already registed...!'
            elif mobile_exist:
                email_error = 'Mobile has already registed...!'    
            else:
                user.save()
                return redirect('/account/login')    
    else:
        form = UserRegistration()        

    return render(request,'account/registration.html',{'form':form,'email_error':email_error})

def login(request):
    email_error = None
    if request.method =='POST':
        form = UserLogin(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        
        user = User()
        Is_login = user.Login_check(email)
        if Is_login:
            if check_password(password,Is_login.password):
                request.session['user_id'] = Is_login.id
                request.session['user_email'] = Is_login.email
                return redirect('/')
            else:
                email_error = 'Invalid password entered...!'
        else:
            email_error = 'Invalid mail id entered...!'
                
    else:
        form = UserLogin()
    return render(request,'account/login.html',{'form':form,'email_error':email_error})


def logout(request):
    request.session.clear()
    return redirect('/')

