"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('exchangeRate/', views.exchangeRate, name='exchangeRate'),
    path('purchaseInfo/', views.onlineMallInfo, name='onlineMallInfo'),
    path('image/', views.imageSearch, name='imageSearch'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),
    path('moveToSeller/', views.moveToSeller, name='moveToSeller'),
    path('productDetail/', views.productDetail, name='productDetail'),
    path('login/', views.login, name='login'),
    ]
