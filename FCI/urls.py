"""FCI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('check/', views.check, name='check'),
    url('sun/', views.sun, name='sun'),
    url('mon/', views.mon, name='mon'),
    url('tue/', views.tue, name='tue'),
    url('wed/', views.wed, name='wed'),
    url('thu/', views.thu, name='thu'),
    url('days/', views.days, name='days'),
    url('table/', views.table, name='table'),
    url('index/', views.index, name='index'),
    url('login/', views.login_request, name='login'),
    url('register/', views.register, name='register'),
    url('about/', views.about, name='about'),
    url('prof/', views.prof, name='prof'),
    url('contact/', views.contact, name='contact'),
    url('logout/', views.logout_request, name='logout'),
]
