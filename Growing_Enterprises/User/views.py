from django.shortcuts import render

from .forms import UserProfileForm

# Create your views here.

def index(request):
    return render(request, 'User/index2.html')


def register(request):
    ctx = {}
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print('procede a guardarlo')
            # form.save()
    else:
        form = UserProfileForm()

    ctx['form'] = form
    return render(request, 'User/register.html', context=ctx)


def login(request):
    return render(request, 'User/login2.html')