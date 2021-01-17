from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def showformdata(request):
    if request.method == "POST":
        pi = User.objects.get(pk=1)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentRegistration()

    return render(request, 'enroll/userregistration.html', {'form':fm})
