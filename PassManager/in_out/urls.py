from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("login/",views.log,name="login_url"),
    path("register/",views.reg,name="reg_url"),
    path("logout/",views.out,name="out_url"),
]