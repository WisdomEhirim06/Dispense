from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def index(request):
    return render(request, "index.html")

def register(request):
    # if method is Post, then form input is taken
    if request.method == "POST":
        # Inputed fields are received and created
        form = UserCreationForm(request.POST)

        if form.is_valid:
            form.save()
            # Saved and redirected to login page
            return redirect("login")

    else:
        # If method is GET, then display empty form
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def Signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        
        # If fields are filled correctly
        if form.is_valid:
            # data is gotten from a dictionary
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticates if user with username and password exists
            user = authenticate(request, username=username, password=password)

            # If user exists, login
            if user != None:
                login(request, user)
                return redirect("index")
            # Else display error message
            else:
                messages.error(request, "Invalid Username or Password")
        
        # If form wasn't filled properly
        else:
            messages.error(request, "Please correct errors below")
    
    # If method is GET, then display empty page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


