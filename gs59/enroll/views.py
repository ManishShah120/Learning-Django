from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.
def regi(request):
    messages.info(request, "Now you can login")
    messages.success(request, "Update ho gaya hei")
    messages.warning(request, "This is warning")
    messages.error(request, "This is an error")
    fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})
