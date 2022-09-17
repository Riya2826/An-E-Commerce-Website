from django.shortcuts import render,redirect
from .models import Order
from EcommerceApp import views as ecom


def oc(request):
    return render(request,'order_confirmation.html')


def check(request):
    if request.method == 'POST':
        # nam=request.POST.get('na')
        ema=request.POST.get('em')
        siz=request.POST.get('si')
        addr=request.POST.get('ad')
        qua=request.POST.get('qu')
        pl=Order(username=ecom.usrnme,mail=ema,size=siz,address=addr,quantity=qua)
        pl.save()
        return redirect("oc")

    else:
        return render(request,'checkout.html')






