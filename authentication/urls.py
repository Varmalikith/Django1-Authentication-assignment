from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('index',views.home1, name="home1"),
    path('index1',views.home2, name="home2"),
    path('signup',views.signup, name="signup"),
    path('signup1',views.signup1, name="signup1"),
    path('signin',views.signin, name="signin"),
    path('signin1',views.signin1, name="signin1"),
    path('signout',views.signout, name="signout"),
]
 