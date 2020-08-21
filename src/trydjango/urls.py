"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from pages.views import *
from products.views import product_detailed_view, product_create_view
urlpatterns = [
    path('', home_view, name=''),
    path('about/', about_view, name=''),
    path('contact/',contact_view, name=''),
    path('products/', product_detailed_view, name=''),
    path('product_create/', product_create_view, name=''),
    path('admin/', admin.site.urls),
]
