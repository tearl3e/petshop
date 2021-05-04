from django.urls import path
from .views import CreatePost
from .views import post_list
from . import views

urlpatterns = [
    path('blog/', post_list, name='blog')
]
