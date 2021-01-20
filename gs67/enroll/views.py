from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group

# SignUp view Fucntion
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully!!!')
            user = fm.save()
            group = Group.objects.get(name='Editor')
            user.groups.add(group)
    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form':fm})

# Login View Funciton
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form': fm})
    else:
        return HttpResponseRedirect('/dashboard/')


# Dashboard View function
def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/dashboard.html', {'name': request.user.username})
    else:
        return HttpResponseRedirect('/login/')


# Logout view function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
