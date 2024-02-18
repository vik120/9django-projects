from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'congrats {username}, you are successfully register')
            return  redirect('food:index')
    else:
        form = UserCreationForm
        # form = forms.RegisterForm()
    return render(request, 'register.html', context={'form': form})
