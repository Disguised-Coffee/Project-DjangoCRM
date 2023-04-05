from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout #Does what it says
from django.contrib import messages




# Create your views here.
def home(request):
    # Check to see if loggin in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have Been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please try again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


# Btw don't mix your names!
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")