from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'website/index.html')

def weather(request):
    return render(request, 'website/weather.html')

def camps(request):
    return render(request, 'website/camps.html')

def info(request):
    return render(request, 'website/info.html')

def register(request):
    return render(request, 'website/register.html')

def register(request):
    return render(request, 'website/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'website/register.html', {'form': form})

def profile(request):
    return render(request, 'website/profile.html')

@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'website/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'website/edit_profile.html', {'form': form})