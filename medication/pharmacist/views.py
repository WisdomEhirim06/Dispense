from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, "index.html")