from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
]
