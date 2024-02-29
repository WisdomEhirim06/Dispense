from django.urls import path
from . import views

urlpatterns = [
     path("", views.search, name="index"),
     path("register/", views.register, name="register"),
     path("login/", views.Signin, name="login")

 ]