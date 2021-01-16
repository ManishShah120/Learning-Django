from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect


def thankyou(request):
    return render(request, 'enroll/success.html')


# Create your views here.
def showformdata(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print(fm)
            # If you want to see a clean data in a dictionary format
            print(fm.cleaned_data)
            # If you only want to see the required datathen
            name = request.POST['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print('Name: ', name)
            print('Email: ', email)
            print('Password: ', password)
            return HttpResponseRedirect('/enroll/success/')
            # return render(request, 'enroll/success.html', {'name':name})
    else:
        fm = StudentRegistration()

    return render(request, 'enroll/userregistration.html', {'form':fm})
