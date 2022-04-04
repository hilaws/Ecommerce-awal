from pydoc import visiblename
from typing import ValuesView
from unicodedata import name
from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('',views.home,name='home'),
    path('main',views.main,name='main'),
    path('cart',views.cart,name='cart'),
    path('login',views.loginView,name='login'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('order',views.order,name="order"),
    path('help',views.help,name='help'),
    path('story',views.ourStory,name='story'),
    path('sighupform',views.sighnup,name='sighnup'),
    path('product-view',views.view_product,name='view'),
    path('products',views.products,name='products')
]
