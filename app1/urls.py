from django.contrib import admin
from django.urls import path

from app1.views import *
app_name = 'app1'

urlpatterns =[
    path('product_create/',ProductCreate.as_view(),name ='product_create')
]