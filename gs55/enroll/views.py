from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def show_formdata(request):
    fm = StudentRegistration()
    return render(request, 'enroll/uerregistration.html', {'form': fm})
