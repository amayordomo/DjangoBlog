from django.shortcuts import render
from . forms import CustomUserCreationForm

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
    return render(request, 'App_Login/signup.html', context)