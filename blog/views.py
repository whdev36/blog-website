from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from .forms import BloggerCreationForm
from django.contrib.auth.decorators import login_required

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}!')
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.warning(request, 'Account does not exist, please log in.')
    return render(request, 'login.html', {})

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

def register_user(request):
    if request.method == 'POST':
        form = BloggerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to the site.')
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.warning(request, 'Please correct the errors below.')
    else:
        form = BloggerCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    messages.info(request, '')
    return redirect('home')