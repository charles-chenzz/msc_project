from django.urls import path
from .views import *
urlpatterns = [
    # 用户的注册和登陆
    path('login.html', loginView, name='login'),
    path('home/<int:page>.html', homeView, name='home'),
    path('logout.html', logoutView, name='logout'),
]
