"""
URL configuration for django_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django_core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('about-us/',views.aboutUS,name="about"),           #using this name variable to use this in django url tag in html file.
    path('contact/',views.contact,name="contact"),
    # path('course/<courseid>',views.courseDetails),    #Dynamic URL/Route: 3 types: 1.int  2.str  3.slug and if don't know the type then dont have to mention type
    path('services/',views.services,name="services"),       
    path('calculations/',views.calculations,name="calculations"),   
    path("form/",views.form,name='form'),
    path("thank/",views.thank,name='thank'),  
    path("submitform/",views.submitform,name='submitform'),
    path("calculator/",views.calculator,name='calculator'),
    path("evenodd/",views.evenodd,name='evenodd'),
    path("marksheet/",views.marksheet,name='marksheet'),
    
]
