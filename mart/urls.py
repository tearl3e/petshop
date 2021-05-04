from django.urls import path
from .views import home, blog, contact, petmart, all, search, category_detail, product_detail

urlpatterns = [
    path('', home, name='index'),
    path('contact/', contact, name='contact'),
    path('petmart/', petmart, name='petmart'),
    path('allproducts/', all, name='allproducts'),
    path('petmart/search/', search, name='search'),
    path('category/<int:id>', category_detail, name='category_detail'),
    path('product/<int:id>', product_detail, name='product_detail'),

]
