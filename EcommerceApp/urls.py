from django.contrib import admin
from django.urls import path
from . import views
 

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('product',views.product,name='product'),
    path('category',views.category,name='category'),
    path('contactus',views.contactus,name='contactus'),
    path('register',views.register,name='register'),
    path('signin',views.signin,name='signin'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    
    ]
    