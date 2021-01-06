from django.contrib import admin
from django.urls import path
from fcuser.views import home
from . import views

urlpatterns = [
    path('register/',views.register),
    path('login/', views.login),
    path('loout/', views.loout)
]
