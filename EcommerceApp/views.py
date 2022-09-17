from django.shortcuts import render,redirect
from .forms import Registerform
from django.contrib import messages
from .models import Registereduser
from django.core.exceptions import  ObjectDoesNotExist
from productsapp import views 
from django.contrib.auth.mixins import UserPassesTestMixin

def register(request):
    if request.method == "POST":
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
    else:
        form = Registerform()
        user_info = {'form': form}
        return render(request,"register.html",user_info)
def signin(request):
    global usrnme
    if request.method == "POST":
        usrnme = request.POST['username']
        psswrd = request.POST['pswd']
        
        try:
            user = Registereduser.objects.get(name=usrnme)
            if usrnme == user.name and psswrd == user.password:
                return redirect('login')
            else:
                messages.info(request,"INCORRECT PASSWORD")
                return redirect("signin")
        except ObjectDoesNotExist:
            messages.info(request,"THE USER DOES NOT EXIST")
            return redirect("signin")
    else:
        return render(request,"signin.html")


def about(request):
    try:
        if usrnme:
            return render(request,'about.html')
    except NameError:
        return render(request,'about.html')
def index(request):
    try:
        if usrnme:
            userdetails = {"username": usrnme}
            return render(request,'login.html',userdetails)

    except NameError:
        return render(request,'index.html')

    
def contactus(request):
    try:
        if usrnme:
            return render(request,'contact.html')
    except NameError:
        return render(request,'contact.html')
def category(request):
    try:
        if usrnme:
            return render(request,'category.html')
    except NameError:
        return render(request,'category.html')
def product(request):
    try:
        if usrnme:
            return render(request,'product.html')
    except NameError:
        return render(request,'product.html')

def login(request):
    userdetails = {"username" : usrnme}
    return render(request,"login.html",userdetails)



def logout(request):
    global usrnme
    del usrnme
    return render(request,'logout.html')