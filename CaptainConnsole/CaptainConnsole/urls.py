"""CaptainConnsole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include



''' localhost/3000/admin/ '''

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('games/', include('games.urls')),
    path('consoles/', include('consoles.urls')),
    path('cart/', include('cart.urls')),
    path('sales/', include('sales.urls')),
    path('home/', include('home.urls')),
    path('account/', include('account.urls')),
    path('about_us/', include('about_us.urls')),
    path('user/', include('user.urls'))
]
