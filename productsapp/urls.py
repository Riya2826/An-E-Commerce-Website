from django.contrib import admin
from django.urls import path
from . import views
 

urlpatterns=[
    path('check',views.check,name='check'),
    path('oc',views.oc,name='oc'),
    ]