# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

# Models

# Forms
from .forms import UserRegisterForm, EditProfileForm, CaptchaUse

# Create your views here.

def index(request):
    return render(request, 'User/index2.html')


def register(request):
    ctx = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        #brings captcha class here
        form_captcha = CaptchaUse(request.POST)
        if form.is_valid() and form_captcha.is_valid():
            form.save()
    else:
        form = UserRegisterForm()

    ctx['form'] = form
    return render(request, 'User/register.html', context=ctx)


def profile(request):
    ctx = {}
    return render(request, 'User/register.html', context=ctx)


def edit_profile(request):
    ctx = {}
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()

    ctx['form'] = form
    ctx['user'] = request.user
    return render(request, 'User/profile_form.html', context=ctx)


def login(request):
    ctx = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            return redirect('index')

        else:
            ctx['error'] = 'Usuario o contraseña incorrecto'
            ctx['username'] = username

            return render(request,'User/login.html', context=ctx)

    return render(request, 'User/login.html', context=ctx)


def about(request):

    return render(request, 'User/index.html')


def enterprises(request):

    return render(request, 'User/index.html')


def clients(request):

    return render(request, 'User/index.html')