from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("",views.home),
   path("newval",views.addval,name="new_url")
]