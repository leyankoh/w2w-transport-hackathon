from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
# need: home page, user registration page, app booking page

def index(request):
    return render(request, 'wings2wheels/home.html')


def homepage(request): # always pass request for a view
    return render(request = request,
                  template_name="wings2wheels/home.html") # add model here

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # check valid form
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("wings2wheels:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_message[msg])


    form = UserCreationForm
    return render(request, "wings2wheels/register.html", context={"form":form})



