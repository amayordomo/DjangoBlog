from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def signup(request):
    form = CustomUserCreationForm() 
    registered = False  # Flag to check if the user has successfully registered

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            registered = True

    context = {'form': form, 'registered': registered}
    return render(request, 'App_Login/signup.html', context=context)

def login_user(request):
    form = AuthenticationForm()
    context = {'form': form}

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Extract cleaned username and password from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in if authentication is successful
                return HttpResponseRedirect(reverse('index'))  # Redirect to the home page
            else:
                # Add a non-field error to the form if authentication fails
                context['form'].add_error(None, 'Invalid username or password.')

    return render(request, 'App_Login/login.html', context=context)

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))  # Redirect to the login page
