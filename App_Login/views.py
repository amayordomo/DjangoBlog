from django.shortcuts import render
from . forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    form = CustomUserCreationForm()
    registered = False

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    context = {'form' : form, 'registered' : registered}
    return render(request, 'App_Login/signup.html', context=context)


def login_user(request):
    form = AuthenticationForm()
    context = {'form' : form}

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if username is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    return render(request, 'App_Login/login.html', context=context)

@login_required
def logout_user(request):
    logout(request=request)
    return HttpResponseRedirect(reverse('App_Login:login'))


