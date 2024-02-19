from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'congrats {username}, you are successfully register')
            # return  redirect('food:index')
            return redirect('users:login')
    else:
        # form = UserCreationForm
        form = forms.RegisterForm()
    return render(request, 'register.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('food:index')

@login_required
def profile_page(request):
    return render(request, 'profile.html')