from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm, NoteUploadForm
from .models import UserType, Note
from django.core.exceptions import ObjectDoesNotExist




def home(request):
    return render(request, 'home/home.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data['user_type']
            UserType.objects.create(user=user, user_type=user_type)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


def dashboard(request):
    user = request.user
    user_type = None
    notes = None
    form = None

    try:
        user_type = UserType.objects.get(user=user)
        if user_type.user_type == 'teacher':
            notes = Note.objects.filter(user=user)
            form = NoteUploadForm()
        else:
            notes = Note.objects.all()  # All notes available for students
    except UserType.DoesNotExist:
        pass  # No UserType for the user

    return render(request, 'dashboard/dashboard.html', {'user': user, 'user_type': user_type, 'notes': notes, 'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

def about_page(request):
    return render(request, "about/about.html")
