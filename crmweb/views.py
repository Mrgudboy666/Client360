from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    
    #Check the login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate 
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged in")
            return redirect('home')
        else:
            messages.success(request, "There was a error, Please Login again")
            return redirect('home')
    return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged out")
    return redirect('home')


def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate Login
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Signup successfull")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})
    
    return render(request, 'signup.html', {'form':form})