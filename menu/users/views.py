from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from . import  views
# Create your views here.

def register(request):
    form = UserCreationForm
    return render(request, views.register, context={'form': form})